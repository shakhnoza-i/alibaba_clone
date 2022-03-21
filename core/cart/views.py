from rest_framework import viewsets, generics, status

from cart.models import Cart
from cart.serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
