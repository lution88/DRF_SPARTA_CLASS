from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=100)
    content = models.TextField("카테고리 설명")

