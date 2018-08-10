#Sean Irwin
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, FormView, DetailView, CreateView, DeleteView
from bang.models import Training
from bang.forms import TrainingForm
import datetime
from django.http import Http404, HttpResponseRedirect
# from .forms import -- Forms will be imported here

#creates an instance of current date to compare event date with and restrict deletion
now = datetime.date.today()



#creates a reference to link template of html and model to the database and actual object information
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


class TrainingDetailView(DetailView):
    model = Training
    context_object_name = 'training_detail'
    
class TrainingDeleteView(DeleteView):
    model = Training
    success_url = "/bang/training"
    context_object_name = 'training_delete'

    #changes default behavior of delete to disqualify past events from deletion

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if (self.object.end_date > now):
            return super(TrainingDeleteView, self).delete(
                request, *args, **kwargs)
        else:
            raise Http404("Object you are looking for doesn't exist")

class TrainingFormView(FormView):
    """
    API endpoint that allows an employee form to be viewed and edited.
    """

    template_name = 'bang/training_form.html'
    form_class = TrainingForm
    success_url = '/bang/training/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location'] = 'training_form'
        return context

    def form_valid(self, form):
        form.save()
        return super(TrainingFormView, self).form_valid(form)

    

    

