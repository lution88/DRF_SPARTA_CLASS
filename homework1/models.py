import random

from django.db import models


class Author(models.Model):
    first_name = models.CharField("이름", max_length=100)
    last_name = models.CharField("성", max_length=100)
    birthday = models.DateField("생일", null=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Isbn(models.Model):
    isbn = models.CharField("책 교유번호", max_length=13, unique=True, help_text="13자리 고유번호를 적어주세요")

    def __str__(self):
        return self.isbn


class Genre(models.Model):
    name = models.CharField("장르", max_length=200, help_text="장르를 적어주세요.")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField("책 제목", max_length=200)
    # 북 클래스는 오직 한명의 저자만 가질 수 있다. 하지만 저자는 여러가지 책들을 쓸 수 있다. ForeignKey
    author = models.ForeignKey(Author, verbose_name="작가",on_delete=models.SET_NULL, null=True)
    summary = models.TextField("책내용", help_text="책 내용을 간략하게 적어보세요.")
    genre = models.ManyToManyField(Genre, verbose_name="장르", help_text="책에 맞는 장르를 골라주세요.")
    # isbn = 출판되는 책의 고유번호
    isbn = models.OneToOneField(Isbn, verbose_name="고유번호", on_delete=models.CASCADE, help_text="고유번호 고르기", related_name="book_isbn_set",
                                null=True)

    def __str__(self):
        return self.title



