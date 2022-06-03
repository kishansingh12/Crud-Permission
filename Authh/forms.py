
from django.forms import ModelForm
from .models import *
from django import forms

class UserForm(ModelForm):

    class Meta:
        model = User
        fields =  ['mobile', 'username', 'password']

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', False)
        if not self.instance.mobile == mobile:
            return None    
        else:
            forms.ValidationError("This is not valid Mobile already register")    