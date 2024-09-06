# inventario/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventario_list, name='inventario_list'),  # Root path for the inventario app
    path('eliminar/<int:id>/', views.producto_eliminar, name='producto_eliminar'),
]
