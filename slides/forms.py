from django import forms
from .models import Slide

class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['title', 'file']