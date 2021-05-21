from django import forms
from .models import Property
from .models import User
from django.core import validators
from Account.models import User_Registration

class Property_form(forms.ModelForm):
    class Meta:
        model = Property
        # fields = "__all__"
        fields=['photo']
        labels = {'photo':''}


class Property_form2(forms.ModelForm):
    class Meta:
        model = Property
        fields=['p_name','p_city','p_state','email','area_code','phone','p_type','p_address','execting_cus','p_price','p_time_area','p_rooms_available','p_floor_no','p_sharing_member','tenants_preffered','p_amanities','house_rules']

class Userupdateform(forms.ModelForm):
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))
    
    
    class Meta:
        model=User
        fields=['first_name','last_name']

class Userupdateform1(forms.ModelForm):
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Address'}))
    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City'}))
    state = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter State'}))
    profilepic=forms.ImageField(required=False,widget=forms.FileInput(attrs={'class':'profile-pic','alt':'Maxwell Admin'}))
    class Meta:
        model=User_Registration
        fields=['address','city','state','user','profilepic']

        
    