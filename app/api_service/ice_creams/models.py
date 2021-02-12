from django.db import models

from core.models import BaseModel


class ServingCategory:
    """
    An enum for serving types.
    """

    IN_CONE = 1
    IN_500ML_TUB = 2
    IN_1L_TUB = 3
    IN_2L_TUB = 4

    CHOICES = (
        (IN_CONE, 'In Cone'),
        (IN_500ML_TUB, '500ml Tub'),
        (IN_1L_TUB, '1L Tub'),
        (IN_2L_TUB, '2L Tub'),
    )


class Topping(BaseModel):
    """
    A selection of toppings.
    """

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name


class Flavor(BaseModel):
    """
    A flavor of ice cream.
    """

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name


class IceCreamServing(BaseModel):
    """
    A serving of a delicious treat!
    """

    name = models.CharField(max_length=128, blank=True, default='')
    description = models.TextField(blank=True, default='')
    category = models.IntegerField(choices=ServingCategory.CHOICES)

    def __str__(self):
        return self.name


class IceCream(BaseModel):
    """
    A sweet cold treat!
    """

    serving = models.ForeignKey(IceCreamServing, on_delete=models.PROTECT)
    flavor = models.ForeignKey(Flavor, on_delete=models.PROTECT)
    toppings = models.ForeignKey(Topping, on_delete=models.PROTECT)
    order = models.IntegerField()

    def __str__(self):
        return f'{self.serving} | {self.flavor}'
