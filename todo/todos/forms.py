from django import forms
from .models import TodoItem

class ItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ["title","completed"]