from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

from posts.models import Post


class Review(models.Model):
    review_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return str(self.rating) + " | " + self.post.name
