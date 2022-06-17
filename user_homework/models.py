from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserCustomModel(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(username=username, )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    username = models.CharField("사용자계정", max_length=100, unique=True)
    email = models.EmailField("이메일", max_length=100)
    password = models.CharField("패스워드", max_length=200)
    fullname = models.CharField("이름", max_length=20)
    dt_created = models.DateTimeField("가입일", auto_now_add=True)
    dt_updated = models.DateTimeField("수정일", auto_now=True)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    # id로 사용할 필드 지정 / 로그인 시 username필드에 설정된 필드와 password가 사용된다.
    USERNAME_FIELD = 'username'
    # user 생성 시 입력받은 필드 지정
    REQUIRED_FIELDS = []

    objects = UserCustomModel()

    def __str__(self):
        return self.username

    # 로그인 사용자 특정 테이블 CRUD 권한 설정, admin일 경우 항상 True, 비활성 사용자의 경우 항상 False
    def has_perm(self, perm, obj=None):
        return True

    # 로그인 사용자 특정 app에 접근 가능 여부 설정, app_label에 app이름 들어간다.
    # admin일 경우 항상 True, 비활성 사용자의 경우 항상 False
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class UserProfile(models.Model):
    user = models.OneToOneField(Users, verbose_name="사용자", on_delete=models.CASCADE, primary_key=True)
    introduction = models.TextField("소개")
    birthday = models.DateField('생일')
    age = models.IntegerField('나이')

    def __str__(self):
        return f'{self.user.fullname}의 프로필 입니다.'