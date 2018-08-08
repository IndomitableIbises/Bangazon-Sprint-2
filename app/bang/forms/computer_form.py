from django import forms
from bang.models import Computer


class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['make', 'manufacturer', 'purchase_date']