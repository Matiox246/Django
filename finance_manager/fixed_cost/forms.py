from django import forms
from .models import FixedCost

class FixedCostForm(forms.ModelForm):
    class Meta:
        model = FixedCost
        fields = ['title', 'amount', 'schedule', 'custom_schedule', 'deadline', 'custom_deadline']


# def clean(self):
#         cleaned_data = super().clean()
#         schedule = cleaned_data.get('schedule')
#         schedule_custom = cleaned_data.get('schedule_custom')

#         # Validate custom_value only if 'custom' is selected
#         if schedule == 'custom' and not schedule_custom:
#             self.add_error('schedule', 'This field is required when selecting "Custom".')

#         return cleaned_data
