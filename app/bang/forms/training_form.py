from django import forms
from bang.models import Training


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['name', 'description', 'end_date', 'max_attendees']
