from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):

    # Se crea el objeto Cart con la información recibida.
    cart = Cart(request)

    # Se obtiene la información del producto a agregar y los datos del formulario.
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    # Se verifica si el formulario es válido, si es así se procede a agregar el producto.
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return Response(status=status.HTTP_201_CREATED)


def cart_remove(request, product_id):

    # Se crea el objeto Cart con la información recibida.
    cart = Cart(request)

    # Se obtiene la información del producto a remover y se procede a eliminarlo del carrito.
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return Response(status=status.HTTP_204_NO_CONTENT)


def cart_detail(request):

    # Se crea el objeto Cart con la información recibida.
    cart = Cart(request)

    # Se obtiene la información de cada item del carrito para mostrarla
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return JsonResponse([cart], safe=False)

