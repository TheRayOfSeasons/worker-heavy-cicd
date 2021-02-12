from rest_framework import viewsets

from ice_creams.models import Flavor
from ice_creams.models import IceCream
from ice_creams.models import IceCreamServing
from ice_creams.models import Topping

from .serializers import FlavorSerializer
from .serializers import IceCreamSerializer
from .serializers import IceCreamServingSerializer
from .serializers import ToppingSerializer


class ToppingViewSet(viewsets.ModelViewSet):
    """
    Viewset for toppings.
    """
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class FlavorViewSet(viewsets.ModelViewSet):
    """
    Viewset for toppings.
    """
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer


class IceCreamServingViewSet(viewsets.ModelViewSet):
    """
    Viewset for toppings.
    """
    queryset = IceCreamServing.objects.all()
    serializer_class = IceCreamServingSerializer


class IceCreamViewSet(viewsets.ModelViewSet):
    """
    Viewset for toppings.
    """
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer
