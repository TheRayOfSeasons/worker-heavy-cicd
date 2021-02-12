from rest_framework import serializers

from ice_creams.models import Flavor
from ice_creams.models import IceCream
from ice_creams.models import IceCreamServing
from ice_creams.models import Topping


class ToppingSerializer(serializers.ModelSerializer):
    """
    Serializer for toppings.
    """

    class Meta:
        model = Topping
        fields = ['id', 'name', 'description']


class FlavorSerializer(serializers.ModelSerializer):
    """
    Serializer for toppings.
    """

    class Meta:
        model = Flavor
        fields = ['id', 'name', 'description']


class IceCreamServingSerializer(serializers.ModelSerializer):
    """
    Serializer for servings.
    """

    class Meta:
        model = IceCreamServing
        fields = ['id', 'name', 'description']


class IceCreamSerializer(serializers.ModelSerializer):
    """
    Serializer for ice creams.
    """

    class Meta:
        model = IceCream
        fields = ['id', 'serving', 'flavor', 'toppings', 'order']
