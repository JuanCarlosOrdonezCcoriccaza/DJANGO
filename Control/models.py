from django.db import models

# Create your models here.

class Empleado(models.Model):
    idEmpleado = models.CharField(primary_key=True,max_length=5)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=9)

    def _str_(self):
        texto="{0} ({1})"
        return texto.format(self.idEmpleado,self.Nombre)

class Conductor(models.Model):
    idConductor = models.CharField(primary_key=True,max_length=5)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=9)
    Licencia = models.CharField(max_length=10)

    def _str_(self):
        texto="{0} ({1})"
        return texto.format(self.idConductor,self.Nombre)
    
"""
class Vehiculo(models.Model):
    idVehiculo = models.CharField(primary_key=True,max_length=5)
    Placa = models.CharField(max_length=6)
    Conductor = models.CharField(max_length=50)
    Mantenimiento = models.CharField(max_length=9)
    

    def _str_(self):
        texto="{0} ({1})"
        return texto.format(self.idVehiculo,self.Placa)
    """