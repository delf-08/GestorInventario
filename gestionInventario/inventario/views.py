from django.shortcuts import render, redirect
from .inventario import Inventario  # Import your repository class

inventario_articulo = Inventario()

def inventario_list(request):
    productos = inventario_articulo.mostrar()
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        precio = float(request.POST.get('precio'))
        unidad = int(request.POST.get('unidad'))
        inventario_articulo.añadir(nombre, precio, unidad)
        return redirect('inventario_list')
    return render(request, 'inventario/inventario_list.html', {'productos': productos})

def producto_eliminar(request, id):
    inventario_articulo.eliminar(id)
    return redirect('inventario_list')
