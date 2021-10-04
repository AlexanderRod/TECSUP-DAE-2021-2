from django.shortcuts import get_object_or_404, render

from .models import Producto
from .models import Categoria

# Create your views here.
def index (request):
    product_list = Producto.objects.order_by('nombre')[:6]
    category_list = Categoria.objects.all()
    context = {
        'product_list': product_list,
        'category_list' : category_list
        }
    return render(request, 'index.html', context)

def producto (request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'producto.html', {'producto': producto})
