import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
    location = models.CharField(max_length=300)
    employee_сount = models.PositiveSmallIntegerField (default=0, choices=EMPLOYEE_COUNT)
    transaction_count = models.PositiveIntegerField(default=0) # order_quantity
    transaction_amount = models.PositiveIntegerField(default=0)

    def __str__(self): 
        return self.name
