from rest_framework import serializers

from user.models import User, UserProfile, Hobby
from blog.models import Category, Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer()

    class Meta:
        model = Article
        fields = ["title"]


class BlogUserSerializer(serializers.ModelSerializer):
    article_user = ArticleSerializer(many=True)

    class Meta:
        model = User
        fields = ["username", "join_date", "article_user"]
