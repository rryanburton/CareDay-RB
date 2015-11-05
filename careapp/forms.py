from django.forms import ModelForm
from django.contrib.admin.widgets import AdminTimeWidget

# from django.contrib.auth.models import User

from .models import Child, DailyReport, Diapering
# Create the form class.


class ChildForm(ModelForm):

    class Meta:
        model = Child
        fields = ('first_name', 'gender', 'birthday',
                  'parent_name', 'parent_email', 'parent_phone')

# class EditBookmarkForm(ModelForm):
#     class Meta:
#         model = Bookmark
#         fields = ('title','comment')


class DailyReportForm(ModelForm):

    class Meta:
        model = DailyReport
        fields = ('date', 'child', 'arrival_time', 'departure_time',
                  'mood_am', 'mood_pm')


class DiaperForm(ModelForm):

    class Meta:
        model = Diapering
        fields = ('time_diaper', 'num_one', 'num_two', 'comments')
