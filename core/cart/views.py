from decimal import Decimal

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from posts.models import Post
from cart.models import Cart
from cart.serializers import CartSerializer, CartSumSerializer
from permissions  import OwnerOrReadOnly


class CartCreate(generics.CreateAPIView):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer, **kwargs):
        post_i = serializer.validated_data['post'] # get id instead of string
        post = Post.objects.get(id=post_i)
        user = self.request.user

        serializer.save(user=user, name=post.name, price=post.price)


class CartList(generics.ListAPIView):
    """View all reviews for particular post"""
    serializer_class = CartSumSerializer
    permission_classes = [OwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        cart_queryset = Cart.objects.filter(user=user)
        return cart_queryset    


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSumSerializer
    permission_classes = [OwnerOrReadOnly]
