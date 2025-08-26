from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    queryset = Property.objects.all()
    data = serializers.serializer('json', queryset)
    return JsonResponse(data, safe=False)
