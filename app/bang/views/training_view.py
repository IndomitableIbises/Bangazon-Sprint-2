#Sean Irwin
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, FormView, DetailView, CreateView, DeleteView, UpdateView
from bang.models import Training
from bang.forms import TrainingForm
import datetime
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.exceptions import ImproperlyConfigured
from django.forms import models as model_forms
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from django.views.generic.detail import (
    BaseDetailView, SingleObjectMixin, SingleObjectTemplateResponseMixin,
)
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
    
    

class DeletionMixin:
    """Provide the ability to delete objects."""
    success_url = None

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        if (self.object.end_date > now):
            self.object.delete()
            return HttpResponseRedirect(success_url)
        else:
            return HttpResponseRedirect(success_url)

    # Add support for browsers which only accept GET and POST for now.
    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        if self.success_url:
            return self.success_url.format(**self.object.__dict__)
        else:
            raise ImproperlyConfigured(
                "No URL to redirect to. Provide a success_url.")

class DeleteEnabledDetailView(DeletionMixin, TrainingDetailView):
    success_url = "/bang/training"
    context_object_name = 'training_delete'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

# class TrainingDeleteView(DeleteView):
#     model = Training
#     success_url = "/bang/training"
#     context_object_name = ''

    #changes default behavior of delete to disqualify past events from deletion

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     if (self.object.end_date > now):
    #         return super(TrainingDeleteView, self).delete(
    #             request, *args, **kwargs)
    #     else:
    #         raise Http404("Object you are looking for doesn't exist")

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

class TrainingUpdate(UpdateView):
    model = Training
    fields = ['name', 'description', 'start_date', 'end_date', 'max_attendees']
    success_url = '/bang/training/'
    

    

