from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
# from user_homework.models import Users, UserProfile


class HobbySerializer(serializers.ModelSerializer):
    """
    Hobby 시리얼라이저 추가하기!
    1. HobbySerializer 선언
    2. UserProfileSerializer 의 필드에 추가.
    3. 쿼리셋이므로 HobbySerializer() 안에 many=True 를 넣어준다.
    """
    same_hobby_users = serializers.SerializerMethodField()
    """
    - 번외: 같은 취미를 공유하는 사람들을 알고 싶을때 
    : serializers의 ModelSerializerMethodField 사용. 메소드필드
    1. 변수 same_hobby_users 를 정하고 serializers.SerializerMethodField() 선언
     - 원하는 데이터는 SerializerMethodField() 를 사용해서 가져온다!!
    2. 변수를 받아오는 get_same_hobby_users 함수를 만들어서 obj를 받는다.
    3. HobbySerializer 의 필드에 same_hobby_users 를 추가해 준다.
    4. user_list 리스트 선언하고 역참조 써서 같은 취미를 가진 유저들을 받아온다.
    """
    def get_same_hobby_users(self, obj):
        user_list = [user_profile.user.username for user_profile in obj.userprofile_set.all()]
        return {"같은 취미를 가진 사람" : [user_list]}


    class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]


class UserProfileSerializer(serializers.ModelSerializer):
    # hobby는 데이터를 직렬화 할 때, get_hobbys는 profile을 등록할 떄 사용된다.
    hobby = HobbySerializer(many=True, required=False)
    get_hobbys = serializers.ListField(required=False)
    # required: 무조건 데이터를 넣지 않아도 된다. "기본값=True"
    """
    지금은 UserSerializer로 유저 프로필 없이 사용자 정보만 보이고 있다.
    유저프로필도 추가해 보자!
    1. 유저프로필에 대한 시리얼라이저 생성
    2. 사용할 모델은 UserProfileModel / fields = "__all__"
    3. UserSerializer 안에 userprofile 선언
    4. 선언한 userprofile 을 UserSerializer 의 필드로 넣어준다.
    """
    class Meta:
        model = UserProfileModel
        # fields = "__all__"
        fields = ["introduction", "birthday", "age", "hobby", "get_hobbys"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer() # 시리얼라이저가 기본적으로 생성을 못해준다 -> 커스텀 create 선언해서 사용.

    # create 함수 선언.
    def create(self, validated_data):
        print(validated_data)
        # object를 생성할때 다른 데이터가 입력되는 것을 방지하기 위해 미리 pop 해준다.
        user_profile = validated_data.pop('userprofile') # 데이터를 뽑기위해 pop을 한다.
        get_hobbys = user_profile.pop("get_hobbys", [])

        # User object 생성
        user = UserModel(**validated_data)
        user.save()

        # UserProfile object 생성
        user_profile = UserProfileModel.objects.create(user=user, **user_profile)

        # hobby 등록
        user_profile.hobby.add(*get_hobbys)
        user_profile.save()

        return user


    class Meta: # meta가 되게 중요하다! 시리얼라이저에 들어가는 모든 설정을 관리한다
        # serializer에 사용될 model, field 지정
        model = UserModel
        # fields = 전부일 시 '__all__', 일부 지정 시 리스트나 튜플로 설정 ["username", "password"...], ("username", "password"...)
        fields = ["username", "password", "fullname", "email", "join_date", "userprofile"]
        # fields = "__all__"
        # extra_kwargs : 이 안에서 필드들에 대한 설정을 할 수 있다.
        extra_kwargs = {
            'password': {'write_only': True}, # 패스워드는 write_only 로 쓰기전용으로 사용한다 설정! read하지 않겠다!
            'email': {
                # error_messages : 에러 메세지를 자유롭게 설정 할 수 있다.
                'error_messages': {
                    # required : 값이 입력되지 않았을 때 보여지는 메세지
                    'required': '이메일을 입력해주세요.',
                    # invalid : 값의 포맷이 맞지 않을 때 보여지는 메세지
                    'invalid': '알맞은 형식의 이메일을 입력해주세요.'
                },
                # required : validator에서 해당 값의 필요 여부를 판단한다.
                'required': False  # default : True
            },
        }
