from django import forms
# from django.contrib.auth.models import User
# from extra_views import InlineFormSet
# from django.forms import inlineformset_factory
# from datetimewidget.widgets import TimeWidget
from .models import Child, DailyReport, Diapering, Sleeping, Eating
from functools import partial

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


# class DiaperingFormSet(InlineFormSet):
#
#     model = Diapering
#     fields = ('time_diaper', 'num_one', 'num_two', 'comments')
#     extra = 1
#     widgets = {
#         'time_diaper': TimeInput(attrs={'length': 6}),
#     }
#
# class SleepingFormSet(InlineFormSet):
#
#     model = Sleeping
#     fields = ('time_slp_start', 'time_slp_end')
#     extra = 1
#     labels = {
#         'time_slp_start': 'Nap Start',
#     }
#
# class EatingFormSet(InlineFormSet):
#
#     model = Eating
#     fields = ('time_eat', 'food', 'leftover')
#     extra = 1


DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=DateInput())
    end_date = forms.DateField(widget=DateInput())
