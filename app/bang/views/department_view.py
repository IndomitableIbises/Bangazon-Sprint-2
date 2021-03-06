#Author: Raf
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, FormView, DetailView
from bang.models import Department
from bang.forms import DepartmentForm


"""
These are all the views for DEPARTMENT
    -List View
    -Form View
    -Detail View
"""

class DepartmentListView(ListView):
    """
    API endpoint that allows all DEPARTMENTS to be viewed.
    """
    model = Department
    context_object_name = 'department_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = 'departments'
        return context

class DepartmentFormView(FormView):
    """
    API endpoint that allows a DEPARTMENT FORM to be viewed.
    """
    template_name = 'bang/department_form.html'
    form_class = DepartmentForm
    success_url = '/bang/departments/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = 'departments_form'
        return context

    def form_valid(self, form):
        form.save()
        return super(DepartmentFormView, self).form_valid(form)

class DepartmentDetailView(DetailView):
    """
    API endpoint that allows a single DEPARTMENT to be viewed as well as the EMPLOYEES assigned to that particular DEPARTMENT.
    """
    model = Department
