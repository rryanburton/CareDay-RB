from django.db import models

# Create your models here.


class Child(models.Model):
    BOY = 'B'
    GIRL = 'G'
    GENDER_CHOICES = (
        (BOY, 'B'),
        (GIRL, 'G'),
    )
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              default=BOY)

    first_name = models.CharField(max_length=10)
    birthday = models.DateField()
    parent_name = models.CharField(max_length=10)
    parent_email = models.EmailField(max_length=254)
    parent_phone = models.CharField(max_length=12)
