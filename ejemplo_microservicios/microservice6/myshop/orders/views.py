from django.core.mail import send_mail
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, OrderItem
from .forms import OrderCreateForm
from .serializers import OrderSerializer
from .cart import Cart

class OrderViewSet(viewsets.ViewSet):

    # Método que se accede por la URL /django
    def list(self, request):
        # Se obtiene la lista de productos.
        order = OrderItem.objects.all()

        now = timezone.now()

        for item in order:
            item.diff = (now - item.order.created)

        # Se crea el serializer y se envía como response
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)
    
    # Método que se accede por la URL /django
    def create(self, request):
        # Se crea el serializer con los datos recibidos
        cart = Cart(request)

        # Si la llamada es por método POST, es una creación de órden.
        if request.method == 'POST':

        # Se obtiene la información del formulario de la orden,
        # si la información es válida, se procede a crear la orden.
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
            
            # Se limpia el carrito con ayuda del método clear()
                cart.clear()
            
            # Llamada al método para enviar el email.
                send(order.id, cart)
                return Response(status=status.HTTP_201_CREATED)
        else:
            form = OrderCreateForm()
        return Response(status=status.HTTP_201_CREATED)

    # Método que se accede por la URL /django/<str:pk>
    def retrieve(self, request, pk=None):
        # Se obtiene el mensaje con ayuda del pk recibido
        order = Order.objects.get(id=pk)
        # Se crea el serializer
        serializer = OrderSerializer(order)
        # Se envía la respuesta a la solicitud
        return Response(serializer.data)

    # Método que se accede por la URL /django/<str:pk>
    def update(self, request, pk=None): 
        # Se obtiene el mensaje con ayuda del pk recibido
        order = Order.objects.get(id=pk)
        # Se crea el serializer con los datos recibidos
        serializer = OrderSerializer(instance=order, data=request.data)
        # Se verifica si el serializer es válido
        serializer.is_valid(raise_exception=True)
        # Se guarda el serializer
        serializer.save()
        # Se envía la respuesta a la solicitud
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # Método que se accede por la URL /django/<str:pk>
    def destroy(self, request, pk=None):
        # Se obtiene el mensaje con ayuda del pk recibido
        orderitem = OrderItem.objects.get(id=pk)
        # Se procede a eliminar el mensaje
        orderitem.delete()

        # Email ------------------------
        subject = 'Order Update'
        message = 'Dear {},\n\nYou have successfully canceled an item. Your order item was:\n\n\n'.format(orderitem.order.first_name)
        body = message + '' + orderitem.product.name
        send_mail(subject, body, 'framworkstest@gmail.com', [orderitem.order.email], fail_silently=False)

        # Se envía la respuesta a la solicitud
        return Response(status=status.HTTP_204_NO_CONTENT)


    def send(order_id, cart):
        # Se obtiene la información de la orden.
        order = Order.objects.get(id=order_id)

        # Se crea el subject del correo.
        subject = 'Order nr. {}'.format(order.id)

        # Se define el mensaje a enviar.
        message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}.\n\n\n'.format(order.first_name,order.id)
        message_part2 = 'Your order: \n\n'
        mesagges = []

        for item in cart:
            msg = ''  + str(item['quantity'])  + 'x ' + str(item['product'])  +'  $' + str(item['total_price']) + '\n'
            mesagges.append(msg)
        
        message_part3 = ' '.join(mesagges)
        message_part4 = '\n\n\n Total: $'+ str(cart.get_total_price())
        body = message + message_part2 + message_part3 + message_part4

        # Se envía el correo.
        send_mail(subject, body, 'framworkstest@gmail.com', [order.email], fail_silently=False)
