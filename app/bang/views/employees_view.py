from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, FormView, DetailView, CreateView
from bang.models import Employees

class EmployeesListView(ListView):
    model = Employees
    context_object_name = 'employees_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = 'employees'
        return context
