from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Product, Cart, ProductoCarrito
import json
from .forms import CartAddProductForm
from rest_framework.views import APIView
from .serializers import ProCarSerializer, ProductSerializer

class CartViewSet(viewsets.ViewSet):

    # Método que se accede por la URL /django
    def list(self, request):
        # Se obtiene la lista de productos.
        pro_car = ProductoCarrito.all()
        # Se crea el serializer y se envía como response
        serializer = ProCarSerializer(pro_car, many=True)
        return Response(serializer.data)
    
    # Método que se accede por la URL /django
    def create(self, request):
        # Se crea el serializer con los datos recibidos
        serializer = ProCarSerializer(data=request.data)
        # Se verifica si el serializer es válido
        serializer.is_valid(raise_exception=True)
        # Se guarda el serializer
        serializer.save()
        # Se envía la respuesta de la solicitud
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Método que se accede por la URL /django/<str:pk>
    def retrieve(self, request, pk=None):
        # Se obtiene el mensaje con ayuda del pk recibido
        pro_car = ProductoCarrito.objects.get(id=pk)
        # Se crea el serializer
        serializer = ProCarSerializer(pro_car)
        # Se envía la respuesta a la solicitud
        return Response(serializer.data)

    # Método que se accede por la URL /django/<str:pk>
    def update(self, request, pk=None): 
        # Se obtiene el mensaje con ayuda del pk recibido
        pro_car = ProductoCarrito.objects.get(id=pk)
        # Se crea el serializer con los datos recibidos
        serializer = ProCarSerializer(instance=pro_car, data=request.data)
        # Se verifica si el serializer es válido
        serializer.is_valid(raise_exception=True)
        # Se guarda el serializer
        serializer.save()
        # Se envía la respuesta a la solicitud
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # Método que se accede por la URL /django/<str:pk>
    def destroy(self, request, pk=None):
        # Se obtiene el mensaje con ayuda del pk recibido
        pro_car = ProductoCarrito.objects.get(id=pk)
        # Se procede a eliminar el mensaje
        pro_car.delete()
        # Se envía la respuesta a la solicitud
        return Response(status=status.HTTP_204_NO_CONTENT)