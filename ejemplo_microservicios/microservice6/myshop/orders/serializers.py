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
#           |    ModelSerializer    |    serializer del       |    los campos a        |
#           |                       |    modelo Model.        |    utilizar.           |
#           |                       |                         |                        |
#           +-----------------------+-------------------------+------------------------+
#
#-------------------------------------------------------------------------

from rest_framework import serializers
from .models import Order, OrderItem

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        model = OrderItem
        fields = '__all__'