from datetime import timedelta
from django.utils import timezone

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from homework1.models import Book


class CanMakeBook(BasePermission):
    message = '가입일 기준 12시간은 지나야 도서api에 접근이 가능합니다.'

    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.dt_created < (timezone.now() - timedelta(hours=12)))
        return result


class BookApi(APIView):
    permission_classes = [CanMakeBook]

    def get(self, request):
        books = Book.objects.all()
        idx_book = {}
        for idx, book in enumerate(books):
            idx_book[idx] = book.title
        print(idx_book)
        return Response(idx_book)

    def post(self, request):
        title = request.data.get('title', '')
        summary = request.data.get('summary', '')

        new_book = Book.objects.create(
            title=title,
            summary=summary
        )
        new_book.save()

        return Response({new_book.title: "saved"})
