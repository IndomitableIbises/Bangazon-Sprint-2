#Author: Erin Agobert
from django.views.generic import ListView, DetailView, FormView
from bang.models import Computer
from bang.forms import ComputerForm


class ComputerListView(ListView):
    """ View represents a list of employee computers"""
    model = Computer
    context_object_name = 'computer_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = "computers"
        return context

class ComputerDetailView(DetailView):
    """View represents a detail view of an assigned computer"""
    model = Computer

class ComputerFormView(FormView):
    """
    API endpoint that allows a COMPUTER FORM to be viewed and edited.
    """
    template_name = 'bang/computer_form.html'
    form_class = ComputerForm
    success_url = '/bang/computers/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = 'computer_form'
        return context

    def form_valid(self, form):
        form.save()
        return super(ComputerFormView, self).form_valid(form)