from decimal import Decimal

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from posts.models import Post
from cart.models import Cart
from cart.serializers import CartSerializer, CartSumSerializer


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
    permission_classes = [IsAdminUser]
    def list(self, request):
        user = self.request.user
        cart_queryset = Cart.objects.filter(user=user)
        total_sum = sum(Decimal(item.price) * item.quantity for item in cart_queryset)
        return Response(total_sum)     


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSumSerializer
    permission_classes = [IsAdminUser]
