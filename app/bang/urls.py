from django.urls import path
from .views import training_view
from . import views


app_name = 'bang'
urlpatterns = [
    path('training/', training_view.TrainingListView.as_view(), name='training'),
    path('', views.IndexView.as_view(), name = 'index'),
##########
# COMPUTER PATHS by Erin
    path('computers/', views.ComputerListView.as_view(), name='computer_list'),
    path('computers/<int:pk>/', views.ComputerDetailView.as_view(), name='computer_detail'),
    path('computers/add/', views.ComputerFormView.as_view(), name='computer_form'),
##########
# DEPARTMENT PATHS by Raf
# EMPLOYEES PATHS by Hayley
    path('departments/', views.DepartmentListView.as_view(), name='departments'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/add/', views.DepartmentFormView.as_view(), name='departments_form'),
    path('employees/', views.EmployeesListView.as_view(), name='employees'),
    path('employees/<int:pk>/', views.EmployeesDetailView.as_view(), name='employees_detail'),
    path('employees/add/', views.EmployeesFormView.as_view(), name='employees_form'),
    ]
