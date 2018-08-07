from django.urls import path
from . import views


app_name = 'bang'
urlpatterns = [
    path('computers/', views.ComputerListView.as_view(), name='computer_list'),
    path('computer/<int:pk>/', views.ComputerDetailView.as_view(), name='computer_detail')
]