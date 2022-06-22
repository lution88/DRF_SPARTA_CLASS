from django.urls import path

from . import views


urlpatterns = [
    path('', views.UserApiView.as_view()),
    path('login', views.UserLoginView.as_view()),
]
