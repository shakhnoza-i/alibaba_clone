from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cart.views import CartViewSet


router = DefaultRouter()
router.register('', CartViewSet)

app_name = 'cart'

urlpatterns = [
    path('', include(router.urls))
]