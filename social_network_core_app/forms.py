from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .profile_model import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','image']
