from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, FormView, DetailView, CreateView
from bang.models import Employees

from bang.forms import EmployeesForm

class EmployeesListView(ListView):
    model = Employees
    context_object_name = 'employees_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = 'employees'
        return context

class EmployeesFormView(FormView):
    """
    API endpoint that allows an employee form to be viewed and edited.
    """
    template_name = 'bang/employees_form.html'
    form_class = EmployeesForm
    success_url = '/bang/employees/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = 'employees_form'
        return context

    def form_valid(self, form):
        form.save()
        return super(EmployeesFormView, self).form_valid(form)

class EmployeesDetailView(DetailView):
    model = Employees
