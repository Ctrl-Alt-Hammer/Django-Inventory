from django import forms
from . import models

class CreateInventory(forms.ModelForm):
    class Meta:
        model = models.Inventory
        fields = ['name', 'description', 'quantity', 'price', 'slug', 'banner']