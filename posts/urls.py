from django.urls import path, include
from posts.views import PostList, PostDetail


urlpatterns = [
    path('',  PostList.as_view(), name='posts-list'),
    path('<int:pk>/',  PostDetail.as_view(), name='post-details'),
]
