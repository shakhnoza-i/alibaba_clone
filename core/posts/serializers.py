from rest_framework import serializers
from posts.models import Post

class PostSerializerDisplay(serializers.ModelSerializer):

    currency = serializers.CharField(source='get_currency_display')
    category = serializers.CharField(source='get_category_display')
    availability = serializers.CharField(source='get_availability_display')
    
    class Meta:
        model = Post
        fields = [
            'name', 'price', 'currency', 'min_order', 'measure', 
            'category', 'availability', 'detailed_description', 'image'
        ]


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = "__all__"
