from django.contrib.auth import authenticate, login
from django.db.models import F
from django.shortcuts import render
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from user.models import Hobby, UserProfile, User


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
        print("settings.AUTH_USER_MODEL: ", settings.AUTH_USER_MODEL)
        # 정참조
        '''
        user_profile = UserProfile.objects.get(user=1)
        print("정참조")
        print("user_profile.user: ", user_profile.user)
        print("user_profile.hobby: ", user_profile.hobby)
        '''

        # 역참조
        print("역참조")
        '''
        hobby = Hobby.objects.get(id=1)
        hobby.userprofile_set
        '''

        user = User.objects.get(id=1)

        hobby_s = user.userprofile.hobby.all()
        for hobby in hobby_s:
            # exclde : 매칭 된 쿼리만 제외, filter와 반대
            # annotate : 필드 이름을 변경해주기 위해 사용, 이 외에도 원하는 필드를 추가하는 등 다양하게 활용 가능
            # values / values_list : 지정한 필드만 리턴 할 수 있음. values는 dict로 return, values_list는 tuple로 ruturn
            # F() : 객체에 해당되는 쿼리를 생성함
            hobby_members = hobby.userprofile_set.exclude(user=user).annotate(username=F('user__username')).values_list("username", flat=True)
            hobby_members = list(hobby_members)

            print(f'hobby : {hobby.name} / 역참조 hobby members : {hobby_members}')


        #
        #     # break
        # # Hobby 조회
        # # DoesNotExist 핸들링
        # try:
        #     hobby = Hobby.objects.get(id=5)
        #     print(hobby)
        # except Hobby.DoesNotExist:
        #     # object가 존재하지 않을 때 이벤트
        #     return Response({"error": "오브젝트가 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)  # event 발생 시 나타낼 status 직접 지정도 가능하다
        return Response({"message": "get success!!"})


    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!"}, status=status.HTTP_200_OK)