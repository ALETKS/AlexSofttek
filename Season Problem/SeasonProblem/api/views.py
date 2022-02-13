# from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import SeasonClass

import json

# Create your views here.


class SeasonView (View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            season = list(SeasonClass.objects.filter(id=id).values())
            if len(season) > 0:
                season = season[0]
                datos = {'message': "Success", 'season': season}
            else:
                datos = {'message': "season not Found.. ."}
            return JsonResponse(datos)
        else:
            season = list(SeasonClass.objects.values())
            if len(season) > 0:
                datos = {'message': "Success", 'season': season}
            else:
                datos = {'message': "season not Found.. ."}
            return JsonResponse(datos)

    