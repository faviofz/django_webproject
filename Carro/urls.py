from Carro.views import eliminar_producto
from django.urls import path
from Carro import views

app_name="carro"

urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto, name="Agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="Eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="Restar"),
    path("limpiar/", views.limpiar_carro, name="Limpiar"),
]
