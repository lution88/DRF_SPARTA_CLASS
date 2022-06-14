from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


# Create your views here.
from user.models import Hobby


class MyGoodPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated and user.permissions_rank > 5)
        return result


class UserApiView(APIView):
    permission_classes = [permissions.AllowAny]
    # permission_classes = [MyGoodPermission]

    def get(self, request):
        # Hobby 조회
        hobby_list = Hobby.objects.filter(id__gt=5)
        print(hobby_list)

        return Response({"message": "get success!!"})