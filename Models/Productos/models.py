from django.db import models


class Categoria(models.Model):
    Nombre_de_categoria= models.CharField(max_length=100, null=False, unique=True, verbose_name='nombre de categoria')
    def str (self):
       return self.Nombre_de_categoria

class Marca(models.Model):
    Nombre_de_la_Marca = models.CharField(max_length=100, null=False, unique=True)

    def str (self):
       return self.Nombre_de_la_Marca


class Producto(models.Model):
    Nombre_del_Producto = models.CharField(max_length=75)
    Codigo_del_Producto = models.IntegerField()
    Fecha_de_vencimiento = models.DateTimeField()
    Marca = models.ForeignKey(Marca, null=False, on_delete=models.CASCADE)
    Categoria = models.ForeignKey(Categoria, null=False, on_delete=models.CASCADE)

    def str (self):
       return self.Nombre_del_Producto

