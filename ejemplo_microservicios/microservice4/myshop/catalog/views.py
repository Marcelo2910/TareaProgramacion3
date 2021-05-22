from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):

    # Método que se accede por la URL /django
    def list(self, request):
        # Se obtiene la lista de productos.
        products = Product.objects.all()
        # Se crea el serializer y se envía como response
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    # Método que se accede por la URL /django
    def create(self, request):
        # Se crea el serializer con los datos recibidos
        serializer = ProductSerializer(data=request.data)
        # Se verifica si el serializer es válido
        serializer.is_valid(raise_exception=True)
        # Se guarda el serializer
        serializer.save()
        # Se envía la respuesta de la solicitud
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Método que se accede por la URL /django/<str:pk>
    def retrieve(self, request, pk=None):
        # Se obtiene el mensaje con ayuda del pk recibido
        product = Product.objects.get(id=pk)
        # Se crea el serializer
        serializer = ProductSerializer(product)
        # Se envía la respuesta a la solicitud
        return Response(serializer.data)

    # Método que se accede por la URL /django/<str:pk>
    def update(self, request, pk=None): 
        # Se obtiene el mensaje con ayuda del pk recibido
        product = Product.objects.get(id=pk)
        # Se crea el serializer con los datos recibidos
        serializer = ProductSerializer(instance=product, data=request.data)
        # Se verifica si el serializer es válido
        serializer.is_valid(raise_exception=True)
        # Se guarda el serializer
        serializer.save()
        # Se envía la respuesta a la solicitud
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # Método que se accede por la URL /django/<str:pk>
    def destroy(self, request, pk=None):
        # Se obtiene el mensaje con ayuda del pk recibido
        product = Product.objects.get(id=pk)
        # Se procede a eliminar el mensaje
        product.delete()
        # Se envía la respuesta a la solicitud
        return Response(status=status.HTTP_204_NO_CONTENT)