from django.db import models

# Create your models here.
class dominios(models.Model):
	codigo = models.DecimalField(max_digits=10, decimal_places=0)
	dominio = models.CharField(max_length=30)
	fecha_compra = models.DateField()
	duracion = models.CharField(max_length=30)
	fecha_vencimiento = models.DateField()



class hosting(models.Model):
	codigo = models.DecimalField(max_digits=10, decimal_places=0)
	plan = models.CharField(max_length=30)
	dominio_principal = models.CharField(max_length=30)
	fecha_compra = models.DateField()
	duracion = models.CharField(max_length=30)
	fecha_vencimiento = models.DateField()