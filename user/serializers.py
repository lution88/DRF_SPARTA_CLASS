from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from user_homework.models import Users, UserProfile


"""
지금은 UserSerializer로 유저 프로필 없이 사용자 정보만 보이고 있다.
유저프로필도 추가해 보자!
1. 유저프로필에 대한 시리얼라이저 생성
2. 사용할 모델은 UserProfileModel / fields = "__all__"
3. UserSerializer 안에 userprofile 선언 
4. 선언한 userprofile 을 UserSerializer 의 필드로 넣어준다.
"""


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta: # meta가 되게 중요하다! 시리얼라이저에 들어가는 모든 설정을 관리한다
        # serializer에 사용될 model, field 지정
        model = UserModel
        # fields = 전부일 시 '__all__', 일부 지정 시 리스트나 튜플로 설정 ["username", "password"...], ("username", "password"...)
        fields = ["username", "password", "fullname", "email", "join_date", "userprofile"]
        # fields = "__all__"
        # extra_kwargs : 이 안에서 필드들에 대한 설정을 할 수 있다.
        extra_kwargs = {
            'password': {'write_only': True}, # 패스워드는 write_only 로 쓰기전용으로 사용한다 설정! read하지 않겠다!
        }


