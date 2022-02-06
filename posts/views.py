from rest_framework import generics
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from posts.models import Post
from posts.serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer   
    filter_backends = (filters.DjangoFilterBackend, SearchFilter ,OrderingFilter)
    filter_fields = ('currency', 'category', 'availability',)
    ordering =('price',)
    search_fields =('name', 'detailed_description',)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
