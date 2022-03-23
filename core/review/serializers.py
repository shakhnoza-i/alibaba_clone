from rest_framework import serializers
from review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
     
    class Meta:
        model = Review
        exclude = ('post',)
