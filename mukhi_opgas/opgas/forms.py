from django import forms
from .models import Property

class ImageForm(forms.ModelForm):
    class Meta:
        model = Property
        # fields = "__all__"
        fields=['photo']
        labels = {'photo':''}