#Author: Raf
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, FormView, DetailView, CreateView
from bang.models import Department
from bang.forms import DepartmentForm


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

class DepartmentFormView(FormView):
    """
    API endpoint that allows a DEPARTMENT FORM to be viewed and edited.
    """
    template_name = 'bang/department_form.html'
    form_class = DepartmentForm
    success_url = '/bang/departments/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = 'departments'
        return context

    def form_valid(self, form):
        form.save()
        return super(DepartmentFormView, self).form_valid(form)

class DepartmentDetailView(DetailView):
    model = Department