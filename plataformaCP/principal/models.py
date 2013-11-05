from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Dominio(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=0)
    usuario = models.ForeignKey(User)
    dominio = models.CharField(max_length=30)
    fecha_compra = models.DateField()
    duracion = models.CharField(max_length=30)
    fecha_vencimiento = models.DateField()

    def expiring_time(self):
        today_date = datetime.date.today()
        days_count = (self.fecha_vencimiento - today_date).days
        
        if days_count < 0:
            days_to_expire = 'black_alarm'
        elif days_count <= 30:
            days_to_expire = 'red_alarm'
        elif days_count <= 45:
            days_to_expire = 'orange_alarm'
        elif days_count > 45:
            days_to_expire = 'green_alarm'
        else:
            days_to_expire = 'black_alarm'
        
        return days_to_expire
    
    def __unicode__(self):
        return "%s" % (self.dominio)


class Hosting(models.Model):
    codigo = models.DecimalField(max_digits=10, decimal_places=0)
    usuario = models.ForeignKey(User)
    plan = models.CharField(max_length=30)
    dominio_principal = models.CharField(max_length=30)
    fecha_compra = models.DateField()
    duracion = models.CharField(max_length=30)
    fecha_vencimiento = models.DateField()

    def expiring_time(self):
        today_date = datetime.date.today()
        days_count = (self.fecha_vencimiento - today_date).days
        
        if days_count < 0:
            days_to_expire = 'black_alarm'
        elif days_count <= 30:
            days_to_expire = 'red_alarm'
        elif days_count <= 45:
            days_to_expire = 'orange_alarm'
        elif days_count > 45:
            days_to_expire = 'green_alarm'
        else:
            days_to_expire = 'black_alarm'
        
        return days_to_expire

    def __unicode__(self):
        return "%s - %s" % (self.dominio_principal, self.usuario)