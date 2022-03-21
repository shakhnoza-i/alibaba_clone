from django.conf import settings
from django.db import models
from posts.models import Post


class Cart(models.Model):
    """Cart object"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # post = only one for multiply with quantity
    name = models.CharField(default=None, max_length=100) # post is necessary - unique
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.IntegerField(default=1)
