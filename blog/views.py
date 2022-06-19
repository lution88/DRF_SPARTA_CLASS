from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.serializers import BlogUserSerializer


class UserAPIView(APIView):

    def get(self, request):
        user = request.user
        return Response(BlogUserSerializer(user).data, status=status.HTTP_200_OK)


