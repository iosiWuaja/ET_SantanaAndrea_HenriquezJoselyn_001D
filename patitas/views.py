from django.shortcuts import render
from .models import Producto, Categoria
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    producto = Producto.objects.all()
    context={'productos':producto}
    return render(request, 'patitas/index.html', context)

def descuentos(request):
    context={}
    return render(request, 'patitas/descuentos.html', context)

def carrito(request):
    context={}
    return render(request, 'patitas/carrito.html', context)

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