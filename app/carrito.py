from _typeshed import Self
from decimal import Decimal
import decimal
from django.conf import settings
from .models import Producto

class Carrito(object):
    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get(settings.CARRITO_SESSION_ID)
        if not carrito:
            carrito = self.session[settings.CARRITO_SESSION_ID] = {}
        self.carrito = carrito
    
    def agregar(self, producto, cantidad=1, override_cantidad = False):
        producto_id = str (producto.id)
        if producto_id not in self.carrito:
            self.carrito[producto_id] = {'cantidad': 0,
                                        'precio': str(producto.precio)}
        if override_cantidad:
            self.carrito[producto_id]['cantidad'] = cantidad
        else:
            self.carrito[producto_id]['cantidad'] += cantidad
        self.saved
    
    def save(self):
        self.session.modified = True
    
    def remover(self,producto):
        producto_id = str(producto.id)
        if producto_id in self.carrito:
            del self.carrito[producto_id]
            self.saved()
    
    def __iter__(self):
        ids_producto = self.carrito.keys()
        productos = Producto.objects.filter(id__in = ids_producto)
        carrito = self.carrito.copy()
        for producto in productos:
            carrito[str(producto.id)]['producto'] = producto
        for item in carrito.values():
            item['precio'] = Decimal(item['precio'])
            item['precio_total'] = item['precio'] * item['cantidad']
            yield item
    
    def __len__(self):
        return sum(item['precio'] for item in self.carrito.values()) 
    
    def get_precio_total(self):
        return sum(Decimal(item['precio']) * item ['cantidad'] for item in self.carrito.values())
    
    def clear(self):
        del self.session[settings.CARRITO_SESSION_ID]
        self.save()

def carrito(request):

    return{'carrito': Carrito(request)}

class Cart:
    def __init__(self, request):
        self.request = request
        self.request = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
    
    def add(self,producto):
        if str(producto.id) not in self.car.keys():
            self.cart[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "cantidad": 1,
                "precio": str(producto.precio),
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.cart.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    break
        self.save()
    
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True
    
    def remove (self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto.id]
            self.save
    
    def decrement(self, producto):
        for key, value in self.cart.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                if value["cantidad"] < 1:
                    self.remove(producto)
                else:
                    self.save()
                break
            else:
                print("El producto no existe en el carrito")
    
    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True