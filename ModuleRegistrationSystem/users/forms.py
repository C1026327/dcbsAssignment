from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

# Libraries above
# Code Below

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', help_text= 'Your SHU email address. (i.e. A123465)')
    dob = forms.DateField(label='Date of Birth', widget=forms.widgets.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}))


    class meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'dob', 'country', 'city', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']