from django.contrib import admin
from django.urls import path

from .views import CartViewSet

urlpatterns = [
    path('', CartViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    
    path('<str:pk>', CartViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))

]