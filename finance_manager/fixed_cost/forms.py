from django import forms
from .models import FixedCost

class FixedCostForm(forms.ModelForm):
    class Meta:
        model = FixedCost
        fields = ['title', 'amount', 'schedule', 'deadline', 'custom_deadline']


