from django.db import models


class Post(models.Model):

    CURRENCY_CHOICES = (
        ('KZT', ('KZT')),
        ('USD', ('USD')),
        ('EUR', ('EUR')),
        ('RUB', ('RUB')),
        ('CNY', ('CNY')),
    )

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

    name = models.CharField(max_length=100)
    price = models.FloatField(default=0,)
    currency = models.CharField(default='KZT', choices=CURRENCY_CHOICES, max_length=10)
    min_order = models.PositiveIntegerField(default=1,)
    measure = models.CharField(max_length=20)
    category = models.PositiveSmallIntegerField (default=0, choices=CATEGORY_CHOICES)
    availability = models.PositiveSmallIntegerField(default=0, choices=AVAILABILITY_CHOICES)
    detailed_description = models.CharField(max_length=3000, null=True)

    def __str__(self): 
        return self.name
