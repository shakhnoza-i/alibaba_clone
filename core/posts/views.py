from rest_framework.decorators import action # to add custom actions to your viewset
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters import rest_framework as filters

from posts.models import Post
from posts.serializers import PostSerializer, PostSerializerDisplay
from pagination import TenCountPagination
from permissions import OwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet): # this viewset provide all functionality
    """Manage posts in the database"""
    queryset = Post.objects.all()
    filter_backends = (filters.DjangoFilterBackend, SearchFilter ,OrderingFilter)
    filter_fields = ('currency', 'category', 'availability',)
    ordering =('price',)
    search_fields = ('name', 'detailed_description',)
    pagination_class = TenCountPagination

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

    def get_permissions(self):
        """Return appropriate permission class"""
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [OwnerOrReadOnly]
        return [permission() for permission in permission_classes]
