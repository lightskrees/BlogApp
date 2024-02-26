from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from authentication.models import User
from api.serializers import BlogSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from blog.models import Blog


class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Blog.objects.filter(contributors__groups=Group.objects.get(name='authors'))


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return User.objects.all()
