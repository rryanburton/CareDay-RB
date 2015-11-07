from django import forms
# from django.contrib.auth.models import User

from .models import Child, DailyReport, Diapering, Sleeping, Eating
# Create the form class.


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


class DiaperingForm(forms.ModelForm):

    class Meta:
        model = Diapering
        fields = ('time_diaper', 'num_one', 'num_two', 'comments')


class SleepingForm(forms.ModelForm):

    class Meta:
        model = Sleeping
        fields = ('time_slp_start', 'time_slp_end')


class EatingForm(forms.ModelForm):

    class Meta:
        model = Eating
        fields = ('time_eat', 'food', 'leftover')
