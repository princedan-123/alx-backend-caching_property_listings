from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.cache import cache_page
from .models import Property
from .utils import get_all_properties

@cache_page(60 * 15)
def property_list(request):
    queryset = get_all_properties()
    data = serializers.serializer('json', queryset)
    return JsonResponse(data, safe=False)
