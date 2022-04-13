import uuid
import os

from django.conf import settings
from django.db import models


def post_image_file_path(instance, filename):
    """Generate file path for new post image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/post/', filename)


class Post(models.Model):


    CATEGORY_CHOICES = (
        (0, ('Agriculture & Food')),
        (1, ('Apparel,Textiles & Accessories')),
        (2, ('Auto & Transportation')),
        (3, ('Bags, Shoes & Accessories')),
        (4, ('Electronics')),
        (5, ('Electrical Equipment, Components & Telecoms')),
        (6, ('Gifts, Sports & Toys')),
        (7, ('Health & Beauty')),
        (8, ('Home, Lights & Construction')),
        (9, ('Machinery, Industrial Parts & Tools')),
        (10, ('Metallurgy, Chemicals, Rubber & Plastics')),
        (11, ('Packaging, Advertising & Office')),
    )

    AVAILABILITY_CHOICES = (
        (0, ('In stock')),
        (1, ('Will be available soon. Check with the manager')), # datefield
        (2, ('On order')),
        (3, ('Availability unknown')),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(default='KZT', max_length=10)
    min_order = models.PositiveIntegerField(default=1,)
    measure = models.CharField(max_length=20)
    category = models.PositiveSmallIntegerField (default=0, choices=CATEGORY_CHOICES)
    availability = models.PositiveSmallIntegerField(default=0, choices=AVAILABILITY_CHOICES)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    detailed_description = models.CharField(max_length=3000, null=True)
    image = models.ImageField(null=True, upload_to=post_image_file_path)

    def __str__(self): 
        return self.name

    def cost(self):
        return self.price
