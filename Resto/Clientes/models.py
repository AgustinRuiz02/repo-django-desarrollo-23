from django.db import models

class Cliente(models.Model):

    nombre = models.CharField(max_length=50)

    
class Plato(models.Model):
    nombre = models.CharField(max_length=50)


class Orden(models.Model):
    precioT = models.DecimalField(max_digits=10,decimal_places=2)

    
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)

    plato = models.ManyToManyField(Plato)



class Membresia(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, null=True, blank = True)