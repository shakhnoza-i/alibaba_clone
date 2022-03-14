from rest_framework.decorators import action # to add custom actions to your viewset
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters

from posts.models import Post
from posts.serializers import PostSerializer, PostSerializerDisplay


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

    # @action(methods=['POST'], detail=True, url_path='upload-image') # decorator for custom action in viewset
    # def upload_image(self, request, pk=None):
    #     """Upload an image to a post"""
    #     post = self.get_object()
    #     serializer = self.get_serializer(
    #         post,
    #         data=request.data
    #     )

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(
    #             serializer.data,
    #             status=status.HTTP_200_OK
    #         )

    #     return Response(
    #         serializer.errors,
    #         status=status.HTTP_400_BAD_REQUEST
    #     )
