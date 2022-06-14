from django.shortcuts import render
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

# Create your views here.
from user.models import Hobby


class MyGoodPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated and user.permissions_rank > 5)
        return result


class UserApiView(APIView):
    permission_classes = [permissions.AllowAny]
    # permission_classes = [MyGoodPermission]

    def get(self, request):
        # 글로벌 settings의 auth_user_model
        print(settings.AUTH_USER_MODEL)

        # Hobby 조회

        # DoesNotExist 핸들링
        try:
            hobby = Hobby.objects.get(id=500)
        except Hobby.DoesNotExist:
            # object가 존재하지 않을 때 이벤트
            return Response({"error": "오브젝트가 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)  # event 발생 시 나타낼 status 직접 지정도 가능하다

        return Response({"message": "get success!!"})