from django_filters.rest_framework import FilterSet
from .models import Property

class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'property_city': ['exact'],
            'property_type': ['exact'],
            'max_guest': ['gt', 'lt'],
            'price_per_night': ['gt', 'lt'],
        }

