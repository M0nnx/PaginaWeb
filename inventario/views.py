from rest_framework import generics
from .models import Producto
from .serializer import ProductoSerializer
from rest_framework import filters

class addProducto(generics.CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class listProducto(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class buscarId(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class= ProductoSerializer
    filter_backends = [filters.BaseFilterBackend]
    search_fields = ['id','nombre']

    def get_object(self):
        param = self.kwargs.get('param',None)
        try:
            id = int(param)
            return Producto.objects.get(id=id)
        except ValueError:
            try:
                return Producto.objects.get(nombre__iexact=param)
            except Producto.DoesNotExist:
                raise NotFound(f"Producto no encontrado con el nombre: {param}")