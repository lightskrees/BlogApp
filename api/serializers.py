from rest_framework import serializers
from authentication.models import User
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'caption', 'content', 'date_created']


class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']