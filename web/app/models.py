from django.db import models

class Rubro(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    image = models.CharField(max_length=1024, null = True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=40)
    rubro = models.ForeignKey(Rubro, on_delete=models.CASCADE, null=True )

    def __str__(self):
        return self.nombre


class Subproducto(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200,null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    stock = models.IntegerField(null=True)
    precio = models.FloatField(null=True)
    image = models.CharField(max_length=1024, null=True)
    image2 = models.CharField(max_length=1024, null=True)
    image3 = models.CharField(max_length=1024, null=True )

    def __str__(self):
        return self.nombre
    

