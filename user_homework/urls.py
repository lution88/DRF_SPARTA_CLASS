from django.urls import path

from . import views


urlpatterns = [
    path('', views.UserHomeworkApiView.as_view()),
]
