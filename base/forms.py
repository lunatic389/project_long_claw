from django import forms
from django.contrib.auth.models import User
from base.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
        help_texts={'username':None}


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('blood_type','resident_state','date_of_birth','phone_number','registered_as')
        help_texts={'date_of_birth':"(yyyy-mm-dd)"}
