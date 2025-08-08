from django.urls import path
# se importa las vistas de la aplicación
from . import views
# Portafolio_hoel/urls.py (el archivo principal)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
        path('', views.index, name='index'),
        path('proyecto/<int:pk>/', views.detalle_proyecto, name='detalle_proyecto'),
        path('contacto/', views.procesar_contacto, name='contacto'),
 ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)