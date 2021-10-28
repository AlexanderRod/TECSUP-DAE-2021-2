from django.shortcuts import get_object_or_404, render

from .models import Producto
from .models import Categoria

# Create your views here.
def index (request):
    product_list = Producto.objects.order_by('nombre')[:11]
    category_list = Categoria.objects.all()
    context = {
        'product_list': product_list,
        'category_list' : category_list
        }
    return render(request, 'index.html', context)

def producto (request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    context = {
        'producto': producto
        }
    return render(request, 'producto.html',context)

def productoPorCategory (request, categoria_id):
    objCategoria = Categoria.objects.get(pk=categoria_id)
    product_list = Producto.objects.filter(categoria=objCategoria)
    category_list = Categoria.objects.all()
    context = {
        'product_list': product_list,
        'category_list' : category_list
        }
    return render(request, 'index.html', context)

def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')
