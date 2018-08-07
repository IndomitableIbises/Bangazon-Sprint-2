from django.urls import path
from . import views


app_name = 'bang'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),

##########
# DEPARTMENT PATHS by Raf
    path('departments/', views.DepartmentListView.as_view(), name='departments'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/add/', views.DepartmentFormView.as_view(), name='department_form'),]