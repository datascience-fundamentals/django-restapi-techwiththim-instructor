from django.shortcuts import render
from rest_framework import generics, permissions
from .models import BlogPost
from .serializers import BlogPostSerializer

# viewsets -> class from rest_framework, which provides views
# to handle typical CRUD operations for an API


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BlogPostSerializer
