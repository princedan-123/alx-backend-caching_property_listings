from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection

def get_all_properties():
    """A utitlity for low level caching."""
    #  check cache
    queryset = cache.get('all_properties')
    if not cache_result:
        queryset = Property.objects.all()
        cache.set('all_properties', queryset, 3600)
        return queryset
    return queryset

def get_redis_cache_metrics():
    redis = get_redis_connection('default')
    hits = redis.info.get('keyspace_hits', 0)
    misses = redis.info.get('keyspace_misses', 0)
    metrics =  (hits / (hits + misses))
    return {"metrics": metrics}