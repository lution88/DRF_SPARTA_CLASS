from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

from user.models import Hobby as HobbyModel, UserProfile as UserProfileModel, User as UserModel


# admin 꾸미기
class HobbyAdmin(admin.ModelAdmin):
    # admin 페이지에서 보여주는 필드들.
    list_display = ('id', 'name')


class UserProfileInline(admin.StackedInline):
    model = UserProfileModel

    # def formfield_for_manytomany(self, db_field, request, **kwargs):
    #     if db_field.name == 'hobby':
    #         kwargs['queryset'] = HobbyModel.objects.filter(id__lte=7)
    #
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)


class UserAdmin(admin.ModelAdmin):
    list_display = ["id","username","fullname","email"] # 사용자 목록에 보여질 필드 지정.
    list_display_links = ("id", "username", ) # 상세 페이지로 들어갈 수 있는 필드 지정.
    list_filter = ("fullname", ) # 필터를 걸 수 있는 필드 생성.
    search_fields = ("fullname", "username", ) # 검색에 사용될 필드 지정.
    readonly_fields = ("username", "join_date", ) # 상세페이지에서 읽기전용필드를 설정
    fieldsets = (
        ("info", {'fields': ('username', 'fullname', 'join_date')}),
        ('permissions', {'fields': ('is_admin', 'is_active', )}),
    ) # 상세페이지에서 필드를 분류하는데 사용.

    inlines = (
        UserProfileInline,
    )


admin.site.register(HobbyModel, HobbyAdmin)
admin.site.register(UserProfileModel)
admin.site.register(UserModel, UserAdmin)

# unregister
admin.site.unregister(Group)