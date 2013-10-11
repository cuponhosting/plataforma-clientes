from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class dominios(models.Model):
	codigo = models.DecimalField(max_digits=10, decimal_places=0)
	usuario = models.ForeignKey(User)
	dominio = models.CharField(max_length=30)
	fecha_compra = models.DateField()
	duracion = models.CharField(max_length=30)
	fecha_vencimiento = models.DateField()
	
	def __unicode__(self):
		return "%s" % (self.dominio)


class hosting(models.Model):
	codigo = models.DecimalField(max_digits=10, decimal_places=0)
	usuario = models.ForeignKey(User)
	plan = models.CharField(max_length=30)
	dominio_principal = models.CharField(max_length=30)
	fecha_compra = models.DateField()
	duracion = models.CharField(max_length=30)
	fecha_vencimiento = models.DateField()

	def __unicode__(self):
		return "%s - %s" % (self.dominio_principal, self.usuario)