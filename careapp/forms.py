from django import forms
# from django.contrib.auth.models import User

from .models import Child, DailyReport, Diapering, Sleeping, Eating
# Create the form class.

from extra_views import InlineFormSet


class ChildForm(forms.ModelForm):

    class Meta:
        model = Child
        fields = ('first_name', 'gender', 'birthday',
                  'parent_name', 'parent_email', 'parent_phone')


class DailyReportForm(forms.ModelForm):

    class Meta:
        model = DailyReport
        fields = ('date', 'child', 'arrival_time', 'departure_time',
                  'mood_am', 'mood_pm')


class DiaperingFormSet(InlineFormSet):

    model = Diapering
    fields = ('time_diaper', 'num_one', 'num_two', 'comments')
    extra = 1

class SleepingFormSet(InlineFormSet):

    model = Sleeping
    fields = ('time_slp_start', 'time_slp_end')
    extra = 1

class EatingFormSet(InlineFormSet):

    model = Eating
    fields = ('time_eat', 'food', 'leftover')
    extra = 1
