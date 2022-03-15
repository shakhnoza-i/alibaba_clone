from rest_framework.decorators import action # to add custom actions to your viewset
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from posts.models import Post
from posts.serializers import PostSerializer, PostSerializerDisplay


class PostViewSet(viewsets.ModelViewSet): # this viewset provide all functionality
    """Manage posts in the database"""
    queryset = Post.objects.all()
    filter_backends = (filters.DjangoFilterBackend, SearchFilter ,OrderingFilter)
    filter_fields = ('currency', 'category', 'availability',)
    ordering =('price',)
    search_fields =('name', 'detailed_description',)

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'create':
            return PostSerializer
        if self.action == 'update':
            return PostSerializer
        if self.action == 'partial_update':
            return PostSerializer
        if self.action == 'list':
            return PostSerializerDisplay
        if self.action == 'retrieve':
            return PostSerializerDisplay
        if self.action == 'destroy':
            return PostSerializerDisplay
        