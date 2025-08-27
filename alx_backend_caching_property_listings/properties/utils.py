from django.core.cache import cache
from .models import Property

def getallproperties():
    """A utitlity for low level caching."""
    #  check cache
    queryset = cache.get('all_properties')
    if not cache_result:
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)
        return queryset
    return queryset