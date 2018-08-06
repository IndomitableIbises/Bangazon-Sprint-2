from django import forms
from bang.models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']