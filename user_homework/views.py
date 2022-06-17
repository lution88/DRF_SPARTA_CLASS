from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate, login

from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Users, UserProfile
from blog.models import Category, Article


# class CanWriteArticle(permissions.BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         result = bool(user and user.is_authenticated and user.permission_time > user.)


class UserHomeworkApiView(APIView):
    # permission_classes = [CanWriteArticle]
    def get(self, request):
        user = request.user

        print(f"유저 아이디: {user.username}")
        print(f"유저 이메일: {user.email}")
        print(f"유저 이 름: {user.fullname}")


        return Response({"message":'유저정보'})

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "로그인 실패! 유저정보를 확인하세요."}, status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK)


class MakeArticle(APIView):
    def get(self, request):
        user = request.user

        articles = user.article_set.all()
        for article in articles:
            print(f'{article.title}')
        return Response({'message': "article 정보"})

    def post(self, request):
        author = user.username
        title = request.data.get('title', '')
        category = request.data.get('category', '')

