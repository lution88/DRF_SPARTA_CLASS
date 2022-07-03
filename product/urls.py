from django.urls import path

from product.views import EventApiView, EventThumbnailView

urlpatterns = [
    path('', EventApiView.as_view()),
    path('<event_id>/', EventApiView.as_view()),
    path('thumbnail/<event_id>/', EventThumbnailView.as_view()),
]