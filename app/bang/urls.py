from django.urls import path
from .views import training_view
from . import views


app_name = 'bang'
urlpatterns = [
#TRAINING PATHS by Sean
    path('training/', training_view.TrainingListView.as_view(), name='training'),
    path('training_detail/<int:pk>/', training_view.TrainingDetailView.as_view(), name='training_detail'),
    path('training_detail/<int:pk>/training_delete/', training_view.DeleteEnabledDetailView.as_view(), name='training_delete'),
    path('training_detail/<int:pk>/edit', training_view.TrainingUpdate.as_view(), name='training_edit'),
    path('training/add/', training_view.TrainingFormView.as_view(), name='training_form'),
    path('', views.IndexView.as_view(), name = 'index'),
########## 
# COMPUTER PATHS by Erin
    path('computers/', views.ComputerListView.as_view(), name='computer_list'),
    path('computers/<int:pk>/', views.ComputerDetailView.as_view(), name='computer_detail'),
    path('computers/add/', views.ComputerFormView.as_view(), name='computer_form'),
    path('computers/<int:pk>/computer_delete/', views.ComputerDeleteView.as_view(), name='computer_delete'),
##########
# DEPARTMENT PATHS by Raf
    path('departments/', views.DepartmentListView.as_view(), name='departments'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/add/', views.DepartmentFormView.as_view(), name='departments_form'),
##########
# EMPLOYEES PATHS by Hayley
    path('employees/', views.EmployeesListView.as_view(), name='employees'),
    path('employees/<int:pk>/', views.EmployeesDetailView.as_view(), name='employees_detail'),
    path('employees/<int:pk>/edit', views.EmployeesEditView.as_view(), name='employees_edit'),
    path('employees/add/', views.EmployeesFormView.as_view(), name='employees_form')
]
