from django import forms
# from django.contrib.auth.models import User

from .models import Child
# Create the form class.


class ChildForm(forms.ModelForm):

    class Meta:
        model = Child
        fields = ('first_name', 'gender', 'birthday',
                  'parent_name', 'parent_email', 'parent_phone')
