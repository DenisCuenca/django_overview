from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import mascotas

def hello(request):
    mascota = list(mascotas.objects.values())
    return JsonResponse(mascota, safe=False)