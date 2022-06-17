from django.db import models
from user_homework.models import Users


class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=100)
    content = models.TextField("카테고리 설명")

    def __str__(self):
        return f'{self.name} / {self.content}'


class Article(models.Model):
    author = models.ForeignKey(Users, verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("글 제목", max_length=100)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    content = models.TextField("글 내용")

    def __str__(self):
        return f'{self.title} / {self.category.}'