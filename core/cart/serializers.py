from rest_framework import serializers

from cart.models import Cart
# from posts.serializers import PostOrderSerializer


class CartSerializer(serializers.ModelSerializer):

    # name = serializers.StringRelatedField(read_only=True)
    # price = serializers.SlugRelatedField(slug_field='price', read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'product_id', 'name', 'quantity')
        read_only_fields = ('id', 'name')

    def get_name(self):
        return self.product.name

    def get_price(self):
        return self.product.price