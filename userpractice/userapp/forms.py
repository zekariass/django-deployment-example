from django import forms
from django.contrib.auth.models import User
from userapp.models import UserProfileData

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileDataForm(forms.ModelForm):
    class Meta():
        model = UserProfileData
        fields = ('user_portfolio','user_profile_pic')
