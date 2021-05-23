from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from cart import views as viewcart

urlpatterns = [
    path('', include('cart.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)