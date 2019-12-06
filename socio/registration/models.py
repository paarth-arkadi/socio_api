from django.db import models

# Create your models here.
class users_socio(models.Model):
    first_name = models.CharField(max_length=100,blank=True,default=None)
    last_name = models.CharField(max_length=100,blank=True,default=None)