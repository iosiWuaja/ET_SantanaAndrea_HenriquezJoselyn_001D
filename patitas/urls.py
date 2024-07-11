from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('descuentos', views.descuentos, name='descuentos'),
    path('usuario',views.usuario, name='usuario'),
    path('contacto', views.contacto, name="contacto"),
    path('registro', views.registro, name="registro"),

    path('carrito', views.carrito, name="carrito"),
    path('checkout', views.checkout, name='checkout'),

    path('crud', views.crud, name='crud'),
    path('productosAdd', views.productosAdd, name='productosAdd'),
    path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
    path('productos_findEdit/<str:pk>', views.productos_findEdit, name='productos_findEdit'),
    path('productosUpdate', views.productosUpdate, name='productosUpdate'),
]