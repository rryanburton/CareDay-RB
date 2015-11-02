from django.db import models

# Create your models here.


class Child(models.Model):
    first_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    birthday = models.DateField()
    parent_name = models.CharField(max_length=10)
    parent_email = models.EmailField(max_length=254)
    parent_phone = models.CharField(max_length=12)
