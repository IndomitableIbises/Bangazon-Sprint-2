#Author: Erin Agobert
from django.views.generic import ListView, DetailView
from bang.models import Computer
#from .forms import AlbumForm


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