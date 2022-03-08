import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    


class Company(models.Model):

    EMPLOYEE_COUNT = (
        (0, ('< 15 people')),
        (1, ('16 - 100 people')),
        (2, ('101 - 250 people')),
        (3, ('> 250 people')),
    )

    name = models.CharField(max_length=100)
    year_established = models.IntegerField((' year'), validators=[MinValueValidator(1984), max_value_current_year])
    main_products = models.CharField(max_length=1000)
    location = CountryField()
    address = models.CharField(max_length=1000, default=None)
    employee_сount = models.PositiveSmallIntegerField (default=0, choices=EMPLOYEE_COUNT)
    transaction_count = models.PositiveIntegerField(default=0) # order quantity - like book.number_rating
    transaction_amount = models.PositiveIntegerField(default=0) # sum of orders - like book.avg_rating

    def __str__(self): 
        return self.name
