from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from user.models import Hobby as HobbyModel, UserProfile as UserProfileModel, User as UserModel

# admin 꾸미기
class Hobbyadmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(HobbyModel, Hobbyadmin)
admin.site.register(UserProfileModel)
admin.site.register(UserModel)

# unregister
admin.site.unregister(Group)