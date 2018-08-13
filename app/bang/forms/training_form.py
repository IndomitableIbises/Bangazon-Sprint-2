from django import forms
from bang.models import Training


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['name', 'description', 'start_date', 'end_date', 'max_attendees']
