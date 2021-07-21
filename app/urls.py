from app.models import Producto
from django.urls import path
from django.contrib import admin
from django.urls.conf import include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductoViewSet)

urlpatterns = [
    path('', index,name="index"),
    path('contacto/', contacto,name="contacto"),
    path('productos/', productos,name="productos"),
    path('login/', login,name="login"),
    path('registrarse/', registrarse,name="registrarse"),
    path('agregar-productos/', agregar_productos,name="agregar_productos"),
    path('modificar_productos/<id>/', modificar_productos,name="modificar_productos"),
    path('eliminar_productos/<id>/', eliminar_productos,name="eliminar_productos"),
    path('api/', include(router.urls) ),
    path('', include('pwa.urls')),
    
]


admin.site.site_title = "ProyectoSemestral"
admin.site.site_header = "Administracion"
admin.site.site_title = "Modulos de la Aplicacion"

