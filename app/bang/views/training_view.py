#Sean Irwin
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, FormView, DetailView, CreateView
from bang.models import Training
# from .forms import -- Forms will be imported here


class TrainingListView(ListView):
    """
    API endpoint that allows TRAINING to be viewed.
    """
    model = Training
    context_object_name = 'training_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = 'training'
        return context