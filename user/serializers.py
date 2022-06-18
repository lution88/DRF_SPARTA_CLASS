from rest_framework import serializers

from user.models import User as UserModel
from user_homework.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta: # meta가 되게 중요하다! 시리얼라이저에 들어가는 모든 설정을 관리한다
        # serializer에 사용될 model, field 지정
        model = Users
        # fields = 전부일 시 '__all__', 일부 지정 시 리스트나 튜플로 설정 ["username", "password"...], ("username", "password"...)
        fields = ["username", "password", "fullname", "email", "dt_created"]
        # fields = "__all__"
        # extra_kwargs : 이 안에서 필드들에 대한 설정을 할 수 있다.
        extra_kwargs = {
            'password': {'write_only': True}, # 패스워드는 write_only 로 쓰기전용으로 사용한다 설정! read하지 않겠다!
        }
