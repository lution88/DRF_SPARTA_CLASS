import os.path
from datetime import datetime

from django.shortcuts import render
from django.views.static import serve
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from product.serializers import EventSerializer
from product.models import Event


class EventApiView(APIView):
    def get(self, request):
        today = datetime.now().date()
        # 등록된 이벤트 중 현재 시간이 노출 시작 일과 노출 종료 일의 사이에 있고, 활성화 여부가 True인 event 쿼리셋 조회
        events = Event.objects.filter(
            exposure_start_date__lte=today, # start <= today <= end
            exposure_end_date__gte=today,
            is_active=True
        )
        return Response(EventSerializer(events, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        event_serializer = EventSerializer(data=request.data)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data, status=status.HTTP_200_OK)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, event_id):
        event = Event.objects.get(id=event_id)

        event_serializer = EventSerializer(event, data=request.data, partial=True)
        if event_serializer.is_valid():
            event_serializer.save()
            return Response(event_serializer.data, status=status.HTTP_200_OK)
        return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventThumbnailView(APIView):
    def get(self, request, event_id):
        event = Event.objects.get(id=event_id)
        file_path = event.thumbnail.path
        return serve(request, os.path.basename(file_path), os.path.dirname(file_path))