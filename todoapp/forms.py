from django import forms
from .models import Todoapp


class Todoform(forms.ModelForm):
    class Meta:
        model = Todoapp
        fields = ['name', 'priority', 'date']