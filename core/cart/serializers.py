from decimal import Decimal

from rest_framework import serializers

from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'post', 'name', 'price', 'quantity')
        read_only_fields = ('id', 'user', 'name', 'price',)

    def get_name(self):
        return self.post.name

    def get_price(self):
        return self.post.price


class CartSumSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    sum_individual = serializers.SerializerMethodField('individual_sum')

    def individual_sum(self, cart):
        sum_individual = Decimal(cart.price) * cart.quantity
        return sum_individual

    class Meta:
        model = Cart
        fields = ('id', 'user', 'post', 'name', 'price', 'quantity', 'sum_individual')
        read_only_fields = ('id', 'user', 'name', 'price', 'sum_individual')
