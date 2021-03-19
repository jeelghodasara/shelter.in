from django import forms
from .models import Property

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
        # p_name=forms.CharField(max_length=100, required=False)
        # p_city=forms.CharField(max_length=50, required=False)
        # p_state = forms.CharField(max_length=50)
        # email = forms.EmailField(max_length=254)
        # area_code = forms.IntegerField()
        # phone = forms.CharField(max_length=12)
        # p_type = forms.CharField(max_length=50)
        # p_address = forms.CharField(max_length=1024)
        # execting_cus = forms.BooleanField()
        # p_price = forms.IntegerField()
        # p_time_area = forms.CharField(max_length=50)
        # p_rooms_available = forms.IntegerField() 
        # p_floor_no = forms.IntegerField()
        # p_sharing_member = forms.IntegerField()
        # tenants_preffered = forms.CharField(max_length=50)
        # photo = forms.ImageField()
        # p_amanities = forms.CharField(max_length=200)
        # house_rules = forms.CharField(max_length=200)
        # date = forms.DateField()