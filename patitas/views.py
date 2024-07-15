from django.shortcuts import render
from .models import Producto, Categoria, Carrito
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect


@login_required
def menu(request):
    request.session["usuario"]="cliente"
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'patitas/menu.html', context)

def home(request):
    context = {}
    return render(request, 'patitas/index.html', context)

# Create your views here.
def index(request):
    producto = Producto.objects.all()
    context={'productos':producto}
    return render(request, 'patitas/index.html', context)

def descuentos(request): 
    context={}
    return render(request, 'patitas/descuentos.html', context)


def checkout(request):
      context = {}
      return render(request, 'patitas/checkout.html', context)

def usuario(request):
    context={}
    return render(request,'patitas/usuario.html', context)

def contacto(request):
    context={}
    return render(request, 'patitas/contacto.html', context)

def registro(request):
    context={}
    return render(request, 'patitas/registro.html', context)

def crud(request):
    producto = Producto.objects.all()
    context = {'productos':producto}
    return render(request, 'patitas/lista_prod.html', context)

def productosAdd(request):
    if request.method != "POST":
        categorias = Categoria.objects.all()
        context = {'categorias': categorias}
        return render(request, 'patitas/productos_add.html', context)
    else:
        try:
            id = request.POST["id"]
            nombre = request.POST["nombre_prod"]
            descripcion = request.POST["descripcion"]
            categoria_id = request.POST["id_categoria"]
            precio = request.POST["precio"]
            stock = request.POST["stock"]
            imagen = request.FILES.get('imagen')

            objCategoria = Categoria.objects.get(id_categoria=categoria_id)
            producto = Producto(
                id=id,
                nombre_prod=nombre,
                descripcion=descripcion,
                id_categoria=objCategoria,
                precio=precio,
                stock=stock,
                imagen=imagen
            )
            producto.save()

            context = {'mensaje': "Ok, datos grabados...", 'categorias': Categoria.objects.all()}
        except Exception as e:
            context = {'mensaje': f"Error al grabar datos: {str(e)}", 'categorias': Categoria.objects.all()}

        return render(request, 'patitas/productos_add.html', context)

def productos_del(request, pk):
    context={}
    try:
        producto=Producto.objects.get(id=pk)
        
        producto.delete()
        mensaje = "Producto eliminado..."
        productos = Producto.objects.all()
        context={'productos':productos, 'mensaje':mensaje}
        return render(request, 'patitas/lista_prod.html', context)
    except:
        mensaje="Error, ID no existe"
        productos = Producto.objects.all()
        context = {'productos':productos, 'mensaje': mensaje}
        return render(request, 'patitas/lista_prod.html', context)

def productos_findEdit(request, pk):

    if pk != "":
        producto = Producto.objects.get(id=pk)
        categoria = Categoria.objects.all()

        print(type(producto.id_categoria.categoria))

        context = {'producto':producto, 'categoria':categoria}
        if producto:
            return render(request, 'patitas/productos_edit.html',context)
        else:
            context={'mensaje': "Error, ID no existe"}
            return render(request, 'patitas/lista_prod.html', context)

def productosUpdate(request):

    if request.method == "POST":
        id=request.POST["id"]
        nombre=request.POST["nombre"]
        descripcion=request.POST["descripcion"]
        categoria=request.POST["categoria"]
        precio=request.POST["precio"]
        stock=request.POST["stock"]

        objCategoria = Categoria.objects.get(id_categoria = categoria)

        producto = Producto()
        producto.id = id
        producto.nombre_prod = nombre
        producto.descripcion = descripcion
        producto.id_categoria = objCategoria
        producto.precio = precio
        producto.stock = stock
        producto.save()

        categoria= Categoria.objects.all()
        context = {'mensaje': "Datos actualizados", 'categoria':categoria, 'producto':producto }
        return render(request, 'patitas/productos_edit.html', context)
    else:
        productos = Producto.objects.all()
        context = {'productos':productos}
        return render(request, 'patitas/lista_prod.html', context)

@require_POST
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item, created = Carrito.objects.get_or_create(usuario=request.user, producto=producto)

    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()

    return redirect('index')


def ver_carrito(request):
    if request.user.is_authenticated:
        carrito_items = Carrito.objects.filter(usuario=request.user)
        total = sum(item.producto.precio * item.cantidad for item in carrito_items)
        return render(request, 'patitas/carrito.html', {'carrito_items': carrito_items, 'total': total})
    else:
        return redirect('login')

def update_cart(request):
    if request.method == "POST":
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad'))
        producto = Producto.objects.get(id=producto_id)
        carrito_item = Carrito.objects.get(usuario=request.user, producto=producto)

        if cantidad > 0:
            carrito_item.cantidad = cantidad
            carrito_item.save()
        else:
            carrito_item.delete()
        return redirect('carrito')

    else:
        return redirect('index')