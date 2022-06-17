from datetime import timedelta

from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny

from user.models import User


from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Users, UserProfile
from blog.models import Category, Article


class CanWriteArticle(permissions.BasePermission):
    message = '가입일 기준 3분 이상 지난 사용자만 접근 가능합니다.'

    def has_permission(self, request, view):
        user = request.user

        result = bool(user and request.user.dt_created < (timezone.now() - timedelta(minutes=20)))
        print(timezone.now(), timedelta(minutes=2))
        return result


class UserHomeworkApiView(APIView):
    def get(self, request):
        try:
            user = request.user
            print(user)

            print(f"유저 아이디: {user.username}")
            print(f"유저 이메일: {user.email}")
            print(f"유저 이 름: {user.fullname}")

            return Response({"message": '유저정보'})
        except:
            return Response({"message":'로그인 필요'})

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        hashed_password = make_password(password)
        edit_user = Users.objects.get(username=username)
        edit_user.password = hashed_password
        edit_user.save()

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "로그인 실패! 유저정보를 확인하세요."}, status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        return Response({"message": "로그인 성공"}, status=status.HTTP_200_OK)


class MakeArticle(APIView):
    permission_classes = [CanWriteArticle]

    def get(self, request):
        user = request.user
        articles = user.article_set.all()
        for article in articles:
            print(f'{article.title}')
        return Response({'message': "article 정보"})

    def post(self, request):
        user = request.user

        title = request.data.get('title', '')
        content = request.data.get('content', '')
        category = request.data.get('category', '').split(',')

        article = Article.objects.create(
            author=user,
            title=title,
            content=content
        )
        for i in category:
            article.category.add(i)
        return Response("{message: 게시글 생성 성공}", status=status.HTTP_200_OK)