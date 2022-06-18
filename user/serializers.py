from rest_framework import serializers

from user.models import User as UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta: # meta가 되게 중요하다! 시리얼라이저에 들어가는 모든 설정을 관리한다
        # serializer에 사용될 model, field 지정
        model = UserModel
        # fields = 전부일 시 '__all__', 일부 지정 시 리스트나 튜플로 설정 ["username", "password"...], ("username", "password"...)
        fields = ["username", "password", "fullname", "email", "join_date"]
        # fields = "__all__"
