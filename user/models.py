from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# custom user model 사용 시 UserManager 클래스와 create_user, create_superuser 함수가 정의되어 있어야 함


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# 이름만 유저 models.Model , AbstractBaseUser 커스텀 유저모델 : 장고에 등록한 User 변경.
class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=200)
    fullname = models.CharField("이름", max_length=20)
    join_date = models.DateTimeField("가입일", auto_now_add=True)

    # # is_active 가 False 일 경우 계정이 비활성화됨, 로그인 결정
    is_active = models.BooleanField(default=True)

    # is_staff 에서 해당 값 사용, admin 페이지 접근 권한
    is_admin = models.BooleanField(default=False)

    # # id로 사용 할 필드 지정. USERNAME_FILED : 어떤 필드를 ID 로 사용할 것인지 설정.
    # # 로그인 시 USERNAME_FIELD에 설정 된 필드와 password가 사용된다.
    USERNAME_FIELD = 'username'
    #
    # # user를 생성할 때 입력받은 필드 지정
    REQUIRED_FIELDS = []
    #
    objects = UserManager()  # custom user 생성 시 필요

    # 로그인 사용자의 특정 테이블의 crud 권한을 설정, perm table의 crud 권한이 들어간다.
    # admin 일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_perm(self, perm, obj=None):
        return True

    # 로그인 사용자의 특정 app에 접근 가능 여부를 설정, app_label에는 app 이름이 들어간다.
    # admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False
    def has_module_perms(self, app_label):
        return True

    # # admin 권한 설정
    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return f'{self.username} / {self.email}'


class UserProfile(models.Model):
    user = models.OneToOneField(to=User, verbose_name="사용자", on_delete=models.CASCADE, primary_key=True)
    hobby = models.ManyToManyField(to="Hobby", verbose_name="취미")
    introduction = models.TextField("소개")
    birthday = models.DateField("생일")
    age = models.IntegerField("나이")

    def __str__(self):
        return f'{self.user.fullname}님의 프로필입니다.'


class Hobby(models.Model):
    name = models.CharField("취미", max_length=50)

    def __str__(self):
        return self.name