from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Hamburguesa, Ingrediente
import os

# Create your views here.


def form_json_burguer(burguer, ingredientes):
    return {'id': burguer.id, 'nombre': burguer.nombre, 'precio': burguer.precio, 'descripcion': burguer.descripcion, 'imagen': burguer.imagen, 'ingredientes': ingredientes}


def burguer_index(request):
    if request:
        resp = []
        for burguer in Hamburguesa.objects.all():
            ingredientes = []
            for ingredient in burguer.ingredientes.all():
                ingredientes.append(
                    {'path': f'{os.getenv("HOST")}/ingrediente/{ingredient.id}'})
            resp.append(form_json_burguer(burguer, ingredientes))
        response = JsonResponse(resp, safe=False)
    return response


def burguer_detail(request, burguer_id):
    burguer = get_object_or_404(Hamburguesa, pk=burguer_id)
    if request.method == "GET":
        ingredientes = []
        for ingredient in burguer.ingredientes.all():
            ingredientes.append(
                {'path': f'{os.getenv("HOST")}/ingrediente/{ingredient.id}'})
        res = form_json_burguer(burguer, ingredientes)
        return JsonResponse(res, safe=False)
    elif request.method == "PATCH":
        pass
    elif request.method == "DELETE":
        burguer.delete()
        print("Delete")
        return HttpResponse(status=200)


def burguer_ingredient_change(request, burguer_id, ingrediente_id):
    return


def ingredient_index(request):
    return


def ingredient_detail(request, ingredient_id):
    return
