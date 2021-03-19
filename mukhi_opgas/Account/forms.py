from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User_Registration

# class UserRegisterForm(UserCreationForm):
#     model = User_Registration
#     mobile = forms.CharField(max_length=15)

#     class Meta:
#         model = User
#         fields = ['user_type','username','email','mobile_no','password1']

class RegisterForm(forms.Form):
    model = User_Registration
    ut=(
        ('Guest','Guest'),
        ('Owner','Owner')
    )
    user_type=forms.ChoiceField(choices=ut,initial='Guest',required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    # password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile_no = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Mobile Number'}), required=False)
