from django import forms
from . models import tasktab

class todoform(forms.ModelForm):
    class Meta:
        model=tasktab
        fields=['name','priority','date']