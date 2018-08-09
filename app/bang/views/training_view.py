#Sean Irwin
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, FormView, DetailView, CreateView, DeleteView
from bang.models import Training
import datetime
from django.http import Http404, HttpResponseRedirect
# from .forms import -- Forms will be imported here
now = datetime.date.today()



    
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
    
class TrainingDeleteView(DeleteView):
    model = Training
    success_url = "/bang/training"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if (self.object.end_date > now):
            return super(TrainingDeleteView, self).delete(
                request, *args, **kwargs)
        else:
            raise Http404("Object you are looking for doesn't exist")

    

