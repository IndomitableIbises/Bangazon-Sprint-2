from django import forms
from bang.models import Employees


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['first_name', 'last_name', 'start_date', 'department', 'supervisor', 'computer']

#########
# Author: Raf
class EmployeesEditForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['last_name', 'department', 'computer'] # Still need to add training