#Author: Raf
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, FormView, DetailView, CreateView
from bang.models import Department
# from .forms import -- Forms will be imported here


class DepartmentListView(ListView):
    """
    API endpoint that allows DEPARTMENTS to be viewed.
    """
    model = Department
    context_object_name = 'department_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = 'departments'
        return context

# class DepartmentFormView(FormView):
#     template_name = 'bang/department_form.html'