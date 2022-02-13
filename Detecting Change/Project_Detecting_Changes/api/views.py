# from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import WeatherClass

import json


class WeatherView (View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            weather = list(WeatherClass.objects.filter(id=id).values())
            if len(weather) > 0:
                weather = weather[0]
                datos = {'message': "Success", 'weather': weather}
            else:
                datos = {'message': "weather not Found.. ."}
            return JsonResponse(datos)
        else:
            weather = list(WeatherClass.objects.values())
            if len(weather) > 0:
                datos = {'message': "Success", 'weather': weather}
            else:
                datos = {'message': "weather not Found.. ."}
            return JsonResponse(datos)
