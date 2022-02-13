# from django.shortcuts import render
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import OrderClass

import json

# Create your views here.


class OrderView (View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            order = list(OrderClass.objects.filter(id=id).values())
            if len(order) > 0:
                order = order[0]
                datos = {'message': "Success", 'order': order}
            else:
                datos = {'message': "order not Found.. ."}
            return JsonResponse(datos)
        else:
            order = list(OrderClass.objects.values())
            if len(order) > 0:
                datos = {'message': "Success", 'order': order}
            else:
                datos = {'message': "order not Found.. ."}
            return JsonResponse(datos)

    