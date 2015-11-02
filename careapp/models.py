from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
# Create your models here.

# Assume 'dailyreport_id' is defined.


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
    date = models.DateField(default=timezone.now())   # default = Year-Mo-Day
    child = models.ForeignKey(Child)   # Assume '_id' will be added to 'child'
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    mood_am = models.CharField(max_length=2,
                               choices=MOOD_CHOICE,
                               default=HAPPY)
    mood_pm = models.CharField(max_length=2,
                               choices=MOOD_CHOICE,
                               default=HAPPY)

    # def __str__(self):
    #     return ("Name: {}, Date: {}".format(Child.name, date))
