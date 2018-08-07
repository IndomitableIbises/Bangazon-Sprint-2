from django.urls import path
from .views import training_view


app_name = 'bang'
urlpatterns = [
    path('training/', training_view.TrainingListView.as_view(), name='training'),
]