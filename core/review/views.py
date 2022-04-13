from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from permissions import OwnerOrReadOnly
from posts.models import Post
from review.models import Review
from review.serializers import ReviewSerializer


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer): 
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)

        if post.DoesNotExist:
            raise ValidationError("This post does not exist!")

        viewer = self.request.user
        review_queryset = Review.objects.filter(post=post,user=viewer)
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this product!")

        if post.number_rating == 0:
            post.avg_rating = serializer.validated_data['rating']
        else:
            post.avg_rating = (post.avg_rating + serializer.validated_data['rating']) / (post.number_rating + 1)
        
        post.number_rating = post.number_rating + 1
        post.save()

        serializer.save(post=post,user=viewer)
     

class ReviewList(generics.ListAPIView):
    """View all reviews for particular post"""
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(post=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [OwnerOrReadOnly]
