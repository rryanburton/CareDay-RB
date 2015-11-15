from django import forms
# from django.contrib.auth.models import User



from .models import Child, DailyReport, Diapering, Sleeping, Eating
# Create the form class.

from extra_views import InlineFormSet
from django.forms import inlineformset_factory
from datetimewidget.widgets import TimeWidget
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

DiaperingFormSet = inlineformset_factory(DailyReport, Diapering,
                                             fields=('time_diaper', 'num_one', 'num_two', 'comments'),
                                             widgets={
                                                'time_diaper': forms.TimeInput(attrs={'class': 'time_diaper'}),
                                                # 'time_diaper': forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3)),
                                             },
                                             labels={
                                                'time_diaper': 'Potty time',
                                                'num_one': 'Wet',
                                                'num_two': 'BM',
                                             },
                                             extra=1
                                             )

SleepingFormSet = inlineformset_factory(DailyReport, Sleeping,
                                        fields=('time_slp_start', 'time_slp_end'),
                                        widgets={
                                            'time_slp_start': forms.TimeInput(attrs={'class': 'time_slp_start'}),
                                            'time_slp_end': forms.TimeInput(attrs={'class': 'time_slp_end'}),
                                         },
                                        labels={
                                            'time_slp_start': 'Nap time start',
                                            'time_slp_end': 'Nap time finish',

                                         },
                                        extra=1)

EatingFormSet = inlineformset_factory(DailyReport, Eating,
                                         fields=('time_eat', 'food', 'leftover'),
                                         widgets={
                                            'time_eat': forms.TimeInput(attrs={'class': 'time_slp_start'}),
                                         },
                                         labels={
                                            'time_eat': 'Meal time',
                                         },
                                         extra=1)

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
