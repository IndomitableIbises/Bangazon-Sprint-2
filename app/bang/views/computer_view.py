from django.views.generic import ListView
from bang.models import Computer
#from .forms import AlbumForm


class ComputerListView(ListView):
    model = Computer
    context_object_name = 'computer_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = "computers"
        return context