from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from user.models import Hobby as HobbyModel, UserProfile as UserProfileModel, User as UserModel


# admin 꾸미기
class HobbyAdmin(admin.ModelAdmin):
    # admin 페이지에서 보여주는 필드들.
    list_display = ('id', 'name')


admin.site.register(HobbyModel, HobbyAdmin)
admin.site.register(UserProfileModel)
admin.site.register(UserModel)

# unregister
admin.site.unregister(Group)