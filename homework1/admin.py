from django.contrib import admin

# Register your models here.
from homework1.models import Book, Author, Isbn, Genre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Isbn)
admin.site.register(Genre)
