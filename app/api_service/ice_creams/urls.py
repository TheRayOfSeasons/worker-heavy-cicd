from django.urls import include
from django.urls import path

from .views import FlavorsReportView


flavor_patterns = [
    path(
        'report/',
        FlavorsReportView.as_view(),
        name='delegate_flavors_report'
    ),
]


urlpatterns = [
    path('flavors/', include(flavor_patterns))
]
