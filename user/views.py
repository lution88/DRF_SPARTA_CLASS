from django.contrib.auth import authenticate, login
from django.db.models import F
from django.shortcuts import render
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from user.models import Hobby, UserProfile, User
from user.serializers import UserSerializer


class MyGoodPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated and user.permissions_rank > 5)
        return result


class UserApiView(APIView):
    permission_classes = [permissions.AllowAny]
    # permission_classes = [MyGoodPermission]

    def get(self, request):
        """
        모든 사용자에 대해서 user정보와 userprofile 정보를 가져오고
        같은 취미를 가진 사람들 출력하기
        1. 가장 먼저 할 일 : serializers.py 선언
        2. views.py 에 작성한 serializer import UserSerializer
        3. Response에 UserSerializer() 를 적고 안에 "쿼리셋"이나 "인스턴스"를 넣어준다.
        4. UserSerializer(User.objects.all()) 모든 유저에 대해서 UserSerializer를 돌린다.
        5. 쿼리셋으로 넣어주면 뒤에 many=Ture 를 꼭!! 꼭!! 붙여준다.
        6. 그리고 마지막에 .data 를 붙여줘야 JSON 데이터로 나오게 된다.
        7. status code 지정해주기.
        """

        return Response(UserSerializer(User.objects.all().order_by('?').first()).data, status=status.HTTP_200_OK)


    def post(self, request):
        # 로그인 기능
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!"}, status=status.HTTP_200_OK)