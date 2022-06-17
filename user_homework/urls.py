from django.urls import path

from . import views


urlpatterns = [
    path('', views.UserHomeworkApiView.as_view()),
    path('article/', views.MakeArticle.as_view()),
]
