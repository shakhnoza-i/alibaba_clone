from django.conf import settings
from django.db import models
from posts.models import Post


class Cart(models.Model):
    """Cart object"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Post, on_delete=models.CASCADE) # post_id = only one for multiply with quantity
    quantity = models.IntegerField(default=1)
    name = product.__str__
