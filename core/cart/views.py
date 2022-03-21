from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from posts.models import Post
from cart.models import Cart
from cart.serializers import CartSerializer


class CartCreate(generics.CreateAPIView):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        user = self.request.user
        cart_queryset = Cart.objects.filter(post=post, user=user)

        if cart_queryset.exists():
            raise ValidationError("You have already added this product to cart, to change quantity please follow the cart!")

        serializer.save(user=user, name=post.name, price=post.price)


class CartList(generics.ListAPIView):
    """View all reviews for particular post"""
    serializer_class = CartSerializer
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAdminUser]
