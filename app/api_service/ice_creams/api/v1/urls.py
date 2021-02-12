from api_service.urls import router

from .views import FlavorViewSet
from .views import IceCreamViewSet
from .views import IceCreamServingViewSet
from .views import ToppingViewSet


router.register(r'flavors', FlavorViewSet)
router.register(r'ice-creams', IceCreamViewSet)
router.register(r'servings', IceCreamServingViewSet)
router.register(r'toppings', ToppingViewSet)

urlpatterns = []
