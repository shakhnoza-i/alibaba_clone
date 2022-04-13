from rest_framework import serializers
from posts.models import Post

class PostSerializerDisplay(serializers.ModelSerializer):

    category = serializers.CharField(source='get_category_display')
    availability = serializers.CharField(source='get_availability_display')
    
    class Meta:
        model = Post
        fields = [
            'id','name', 'price', 'currency', 'min_order', 'measure', 
            'category', 'availability', 'detailed_description', 
            'avg_rating', 'number_rating', 'image'
        ]
        read_only_fields = ('avg_rating', 'number_rating')


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ('avg_rating', 'number_rating')


class PostOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'name', 'price']
