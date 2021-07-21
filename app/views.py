from sys import excepthook
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UsernameField
from django.core import paginator
from app.forms import ProductoForm
from .forms import CustomUserCreationForm
from django.shortcuts import redirect, render
from .models import Producto
from django.http import Http404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import login as auth_login
from rest_framework import viewsets
from .serializers import ProductoSerializers
# Create your views here.
# Vista para levantar el index
#@login_required

def index(request):
    return render(request,'app/index.html')

def contacto(request):
    return render(request,'app/contacto.html')

def login(request):
    return render(request,'app/login.html')

@login_required
def productos(request):

    productoALL = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productoALL, 3)
        productoALL = paginator.page(page)
    except:
        raise Http404

    datos = {
        'listaProductos' : productoALL,
        'paginator' : paginator
    }
    return render(request,'app/productos.html', datos)



@login_required
def agregar_productos(request):
    datos = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto agregado correctamente"
    
    return render(request,'app/agregar_productos.html', datos)


def modificar_productos(request,id):
    producto = Producto.objects.get(id=id)
    datos = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto modificado correctamente"
            datos['form'] = formulario
    
    return render(request, 'app/modificar_productos.html', datos)

def eliminar_productos(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect(to='productos')


def registrarse(request):
    data = {
        'form' : CustomUserCreationForm()
    } 

    if request.method == 'POST': 
        formulario=CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            user=authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            auth_login(request,user)
        
            data['mensaje'] = "Te has Registrado con Exito crack"
            return redirect(to="index")
        data['form'] = formulario
    
    return render(request,'registration/registrarse.html',data)

class ProductoViewSet (viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializers

# @login_required(login_url='/login')
#def crear_pedido(request):
#    if request.method == 'POST':
#        formulario = CrearPedidoForm(request.POST)
#        if formulario.is_valid():
#            pedido = formulario.save()
#            for item in carrito:
#                DetallePedido.objects.create(pedido = pedido,
#                                            producto = item ['producto'],
#                                            precio = item['precio']
#                                            cantidad = item ['cantidad'])
#            try:
#                enviar_email(request, pedido)
#
#                carrito.clear()
#                return render(request, 'pedido_creado.html', {'pedido': pedido})
#            except:
#                return render (request, "crear_pedido.html", {'carrito': carrito,
#                                                            'formulario': formulario,
#                                                            'pedido_exitoso': False})
#else:
#    formulario =  CrearPedidoForm()
#return render(request, 'crea_pedido.html', {'carrito': carrito, 'formulario'_ formulario})