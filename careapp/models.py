from django.db import models
from django.utils import timezone
from datetime import datetime
# from django.contrib.auth.models import User
# Create your models here.


# Assume 'dailyreport_id' is defined.
class Child(models.Model):
    BOY = 'B'
    GIRL = 'G'
    GENDER_CHOICES = (
        (BOY, 'Boy'),
        (GIRL, 'Girl'),
    )
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              default=BOY)

    first_name = models.CharField(max_length=10)
    birthday = models.DateField()
    parent_name = models.CharField(max_length=10)
    parent_email = models.EmailField(max_length=254)
    parent_phone = models.CharField(max_length=12)

    def __str__(self):
        return ("{} : {}".format(self.first_name, self.gender))


class DailyReport(models.Model):
    HAPPY = 'HA'
    FINE = 'FI'
    LITTLE_FUSSY = 'LF'
    VERY_FUSSY = 'VF'
    NOT_WELL = 'NW'
    MOOD_CHOICE = (
        (HAPPY, 'Happy'),
        (FINE, 'Fine'),
        (LITTLE_FUSSY, 'A Little Fussy'),
        (VERY_FUSSY, 'Very Fussy'),
        (NOT_WELL, 'Not Well'),
    )
    date = models.DateField(default=timezone.now)   # default = Year-Mo-Day
    child = models.ForeignKey(Child)   # Assume '_id' will be added to 'child'
    arrival_time = models.TimeField()
    departure_time = models.TimeField(null=True)
    mood_am = models.CharField(max_length=2,
                               choices=MOOD_CHOICE,
                               default=HAPPY)
    mood_pm = models.CharField(max_length=2,
                               choices=MOOD_CHOICE,
                               default=HAPPY)

    def __str__(self):
        return ("{} : {}".format(self.child.first_name, self.date))


class Diapering(models.Model):
    # assumed diapering_id
    dailyreport_id = models.ForeignKey(DailyReport)
    time_diaper = models.TimeField()
    num_one = models.BooleanField()  # default is None when empty
    num_two = models.BooleanField()
    comments = models.CharField(max_length=100)
