from django.db import models
from user.models import User


class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=100)
    content = models.TextField("카테고리 설명")

    def __str__(self):
        return f'{self.name} / {self.content}'


class Article(models.Model):
    author = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE, related_name="article_user")
    title = models.CharField("글 제목", max_length=100)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    content = models.TextField("글 내용")
    # comment = models.ForeignKey('Comment', verbose_name="댓글", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name="게시글",on_delete=models.CASCADE, related_name="comment_article")
    user = models.ForeignKey(User, verbose_name="작성자",on_delete=models.CASCADE, related_name="comment_user")
    dt_created = models.DateTimeField("작성 시간", auto_now_add=True)
    content = models.TextField("내용")
