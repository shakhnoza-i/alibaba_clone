from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet


router = DefaultRouter()
router.register('', PostViewSet)

app_name = 'posts'

urlpatterns = [
    path('', include(router.urls))
]
