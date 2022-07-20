from django.db import models

# Create your models here.
#Modelo entidad Edicio
class Propietario(models.Model):
    class Meta:       
        verbose_name_plural = "nacionalidad"
    # Opciones atributo tipo edificio   
    opciones_tipo = (
    ('Ecuatoriana','Ecuatoriana'),
    ('Peruana','Peruana'),
    ('Colombiana','Colombiana'),
    )
    nombre = models.CharField(max_length=600)
    apellido = models.CharField(max_length=600)
    edad = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=30, \
            choices= opciones_tipo) 

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.apellido,
                self.edad,
                self.nacionalidad)
        
# Modelo entidad Departamento
class Departamento(models.Model):
    costo = models.DecimalField("Costo del departamento",max_digits=100, decimal_places=2)
    numCuartos = models.IntegerField("numero de cuartos")
    numbanios = models.IntegerField("numero de baños")
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE,
            related_name="propietario")

    def __str__(self):
        return "%s %.2f %d %s" % (self.costo,
                self.numCuartos,
                self.numbanios,
                self.propietario)
