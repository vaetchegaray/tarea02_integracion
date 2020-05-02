from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Hamburguesa, Ingrediente
import os
import json

# Create your views here.


def form_json_burguer(burguer):
    ingredientes = []
    for ingredient in burguer.ingredientes.all():
        ingredientes.append(
            {'path': f'{os.getenv("HOST")}/ingrediente/{ingredient.id}'})
    return {'id': burguer.id, 'nombre': burguer.nombre, 'precio': burguer.precio, 'descripcion': burguer.descripcion, 'imagen': burguer.imagen, 'ingredientes': ingredientes}


def form_json_ingredient(ingredient):
    return {'id': ingredient.id, 'nombre': ingredient.nombre, 'descripcion': ingredient.descripcion}


@csrf_exempt
def burguer_index(request):
    if request.method == "GET":
        resp = []
        for burguer in Hamburguesa.objects.all():
            resp.append(form_json_burguer(burguer))
        response = JsonResponse(resp, safe=False)
        return response
    elif request.method == "POST":
        try:
            body = json.loads(request.body.decode('utf-8'))
            burguer = Hamburguesa(nombre=body["nombre"], precio=body["precio"],
                                  descripcion=body["descripcion"], imagen=body["imagen"])
            burguer.save()
        except:
            return HttpResponse(status=400)
        res = form_json_burguer(burguer)
        return JsonResponse(res, safe=False, status=201)


@csrf_exempt
def burguer_detail(request, burguer_id):
    burguer = get_object_or_404(Hamburguesa, pk=burguer_id)
    if request.method == "GET":
        res = form_json_burguer(burguer)
        return JsonResponse(res, safe=False)
    elif request.method == "PATCH":
        try:
            body = json.loads(request.body.decode('utf-8'))
            burguer.nombre = body["nombre"]
            burguer.precio = body["precio"]
            burguer.descripcion = body["descripcion"]
            burguer.imagen = body["imagen"]
            burguer.save()
        except:
            return HttpResponse(status=400)
        res = form_json_burguer(burguer)
        return JsonResponse(res, safe=False)
    elif request.method == "DELETE":
        burguer.delete()
        return HttpResponse(status=200)


@csrf_exempt
def burguer_ingredient_change(request, burguer_id, ingrediente_id):
    try:
        burguer = Hamburguesa.objects.get(id=burguer_id)
    except:
        return HttpResponse(status=400)
    ingredient = get_object_or_404(Ingrediente, pk=ingrediente_id)
    if request.method == "DELETE":
        try:
            burguer.ingredientes.remove(ingredient)
            burguer.save()
        except:
            return HttpResponse(status=404)
        return HttpResponse(status=200)
    if request.method == "PUT":
        burguer.ingredientes.add(ingredient)
        burguer.save()
        return HttpResponse(status=201)


@csrf_exempt
def ingredient_index(request):
    if request.method == "GET":
        resp = []
        for i in Ingrediente.objects.all():
            resp.append(form_json_ingredient(i))
        response = JsonResponse(resp, safe=False)
        return response
    elif request.method == "POST":
        try:
            body = json.loads(request.body.decode('utf-8'))
            ingredient = Ingrediente(
                nombre=body["nombre"], descripcion=body["descripcion"])
            ingredient.save()
        except:
            return HttpResponse(status=400)
        res = form_json_ingredient(ingredient)
        return JsonResponse(res, safe=False, status=201)


@csrf_exempt
def ingredient_detail(request, ingredient_id):
    ingredient = get_object_or_404(Ingrediente, pk=ingredient_id)
    if request.method == "GET":
        res = form_json_ingredient(ingredient)
        return JsonResponse(res, safe=False, status=200)
    elif request.method == "DELETE":
        if ingredient.hamburguesas.count() == 0:
            ingredient.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=409)
    return HttpResponse(status=400)
