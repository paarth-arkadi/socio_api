from django.db import models

# Create your models here.
class users_socio(models.Model):
    # Stores the socio users TESTING API
    first_name = models.CharField(max_length=100)   # First name of the user
    last_name = models.CharField(max_length=100)    # Last name of the user
    email = models.CharField(max_length=100,default="noid",blank=True)    # Email of the user

"""class socio_users_details(models.Model):
    # Actual model for storage of the users info
    first_name = models.CharField(max_length=100)   # First name of the user
    last_name = models.CharField(max_lenght=100)    # Last name of the user
"""


