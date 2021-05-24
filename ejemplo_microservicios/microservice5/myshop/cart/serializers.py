#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: serializers.py
#
# Implementación de Arquitecturas Micro Servicios.
# Autor(es): Perla Velasco & Jorge Alfonso Solís.
# Version: 1.0.0 Marzo 2021
#
# Descripción:
#
#   En este archivo se definen los serializers de cada modelo de la app
#
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |  - Se indica el modelo |
#           |                       |  - Representa el        |    del serializer y    |
#           |   CartSerializer      |    serializer del       |    los campos a        |
#           |                       |    modelo Cart.         |    utilizar.           |
#           |                       |                         |                        |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |  - Se indica el modelo |
#           |                       |  - Representa el        |    del serializer y    |
#           |   ProCarSerializer    |    serializer del       |    los campos a        |
#           |                       |    modelo               |    utilizar.        |
#           |                       |    ProductoCarrito.     |                        |
#           |                       |                         |                        |
#           +-----------------------+-------------------------+------------------------+
#
#--------------------------------------"-----------------------------------

from rest_framework import serializers
from .models import Cart, ProductoCarrito, Product

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class ProCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoCarrito
        fields = '__all__'
    
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'