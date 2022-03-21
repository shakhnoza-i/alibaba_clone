from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cart.views import CartCreate, CartList, CartDetail


urlpatterns = [
    path('<int:pk>/create/',  CartCreate.as_view(), name='cart-create'),
    path('list/',  CartList.as_view(), name='cart-list'),
    path('detail/<int:pk>/',  CartDetail.as_view(), name='cart-details'),
]