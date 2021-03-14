from django.http import HttpRequest
from django.shortcuts import render

from Models.Productos.forms import FormularioProducto, FormularioMarca, FormularioCategoria
from Models.Productos.models import Producto, Marca, Categoria


class FormularioProductoView(HttpRequest):

    def index(requets):
        producto = FormularioProducto()
        return render(requets, "formularioproducto.html", {"form": producto})

    def procesar_formulario(requets):
        producto = FormularioProducto(requets.POST)
        if producto.is_valid():
            producto.save()
            producto = FormularioProducto()

        return render(requets, "formularioproducto.html", {"form": producto, "mensaje": 'ok'})

    def consultar_producto(requets):
        productos = Producto.objects.all()
        return render(requets, "cproducto.html", {"producto": productos})

    def edit(request, id_producto):
        producto = Producto.objects.filter(id=id_producto).first()
        form = FormularioProducto(instance=producto)
        return render(request, "editproducto.html", {"form": form, 'producto': producto})

    def actualizar_producto(request, id_producto):
        productos = Producto.objects.get(pk=id_producto)
        form = FormularioProducto(request.POST, instance=productos)
        if form.is_valid():
            form.save()
        productos = Producto.objects.all()
        return render(request, "cproducto.html", {"producto": productos})

    def delete(request, id_producto):
        productos = Producto.objects.get(pk=id_producto)
        productos.delete()
        productos = Producto.objects.all()
        return render(request, "cproducto.html", {"producto": productos, "mensaje": 'OK'})



class FormularioMarcaView(HttpRequest):

    def index(requets):
        marca = FormularioMarca()
        return render(requets, "Fmarca.html", {"form": marca})

    def procesar_formulario(requets):
        marca = FormularioMarca(requets.POST)
        if marca.is_valid():
            marca.save()
            marca = FormularioMarca()

        return render(requets, "Fmarca.html", {"form": marca, "mensaje": 'ok'})

    def consultar_marca(requets):
        marcas = Marca.objects.all()
        return render(requets, "cmarca.html", {"marca": marcas})

    def edit(request, id_marca):
        marca = Marca.objects.filter(id=id_marca).first()
        form = FormularioMarca(instance=marca)
        return render(request, "editmarca.html", {"form": form, 'marca': marca})

    def actualizar_marca(request, id_marca):
        marcas = Marca.objects.get(pk=id_marca)
        form = FormularioMarca(request.POST, instance=marcas)
        if form.is_valid():
            form.save()
        marcas = Marca.objects.all()
        return render(request, "cmarca.html", {"marca": marcas})

    def delete(request, id_marca):
        marcas = Marca.objects.get(pk=id_marca)
        marcas.delete()
        marcas = Marca.objects.all()
        return render(request, "cmarca.html", {"marca": marcas, "mensaje": 'OK'})


class FormularioCategoriaView(HttpRequest):

    def index(requets):
        categoria = FormularioCategoria()
        return render(requets, "Fcategoria.html", {"form": categoria})

    def procesar_formulario(requets):
        categoria = FormularioCategoria(requets.POST)
        if categoria.is_valid():
            categoria.save()
            categoria = FormularioCategoria()

        return render(requets, "Fcategoria.html", {"form": categoria, "mensaje": 'ok'})

    def consultar_categoria(requets):
        categorias = Categoria.objects.all()
        return render(requets, "ccategoria.html", {"categoria": categorias})

    def edit(request, id_categoria):
        categoria = Categoria.objects.filter(id=id_categoria).first()
        form = FormularioCategoria(instance=categoria)
        return render(request, "editcategoria.html", {"form": form, 'categoria': categoria})

    def actualizar_categoria(request, id_categoria):
        categorias = Categoria.objects.get(pk=id_categoria)
        form = FormularioCategoria(request.POST, instance=categorias)
        if form.is_valid():
            form.save()
        categorias = Categoria.objects.all()
        return render(request, "ccategoria.html", {"categoria": categorias})

    def delete(request, id_categoria):
        categorias = Categoria.objects.get(pk=id_categoria)
        categorias.delete()
        categorias = Categoria.objects.all()
        return render(request, "ccategoria.html", {"categoria": categorias, "mensaje": 'OK'})
