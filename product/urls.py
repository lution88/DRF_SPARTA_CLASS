from django.urls import path

from product.views import EventApiView

urlpatterns = [
    path('', EventApiView.as_view()),
    path('<event_id>/', EventApiView.as_view()),
]