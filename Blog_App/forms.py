from .models import Blogging
from django import forms

class addblog(forms.ModelForm):
    class Meta:
        model = Blogging
        fields = '__all__'

