"""PrimerParcial2021 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from Models.Productos.views import FormularioProductoView, FormularioMarcaView, FormularioCategoriaView
from Views.homeviews import homeview

urlpatterns = [
    path('', homeview.home, name='home'),

    path('registrarproducto/', FormularioProductoView.index, name='registrarproducto'),
    path('guardarproducto/', FormularioProductoView.procesar_formulario, name='guardarproducto'),
    path('consultarproducto/', FormularioProductoView.consultar_producto, name='Cproducto'),
    path('editarproducto/<int:id_producto>', FormularioProductoView.edit, name='Eproducto'),
    path('actproducto/<int:id_producto>', FormularioProductoView.actualizar_producto, name='Actualizarproducto'),
    path('eliminarproducto/<int:id_producto>', FormularioProductoView.delete, name='eliminarproducto'),

    path('registrarmarca/', FormularioMarcaView.index, name='registrarmarca'),
    path('guardarmarca/', FormularioMarcaView.procesar_formulario, name='guardarmarca'),
    path('consultarmarca/', FormularioMarcaView.consultar_marca, name='Cmarca'),
    path('editarmarca/<int:id_marca>', FormularioMarcaView.edit, name='Emarca'),
    path('actmarca/<int:id_marca>', FormularioMarcaView.actualizar_marca, name='Actualizarmarca'),
    path('eliminarmarca/<int:id_marca>', FormularioMarcaView.delete, name='eliminarmarca'),

    path('registrarcategoria/', FormularioCategoriaView.index, name='registrarcategoria'),
    path('guardarcategoria/', FormularioCategoriaView.procesar_formulario, name='guardarcategoria'),
    path('consultarcategoria/', FormularioCategoriaView.consultar_categoria, name='Ccategoria'),
    path('editarcategoria/<int:id_categoria>', FormularioCategoriaView.edit, name='Ecategoria'),
    path('actcategoria/<int:id_categoria>', FormularioCategoriaView.actualizar_categoria, name='Actualizarcategoria'),
    path('eliminarcategoria/<int:id_categoria>', FormularioCategoriaView.delete, name='eliminarcategoria'),

]
