from django.urls import path
from .views import addProducto, listProducto,buscarId


urlpatterns = [
    path('productos/add/', addProducto.as_view() ,name='añadir-producto'),
    path('productos/view/', listProducto.as_view() ,name='ver-producto'),
    path('productos/view/<str:param>/', buscarId.as_view() ,name='buscarPor'),

]
