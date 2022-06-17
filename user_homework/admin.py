from django.contrib import admin

# Register your models here.
from user_homework.models import UserProfile, Users

admin.site.register(Users)
admin.site.register(UserProfile)