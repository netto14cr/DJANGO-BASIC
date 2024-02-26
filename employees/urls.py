
# Configurated URL patterns for the employees app

# Import the include function
from django.urls import path
# import the views module from the employees app
from . import views

urlpatterns = [

    # Path is the primary key of the employee
    path('<int:pk>/', views.employee_detail, name='employee_detail'), # Add the employee_detail path
    # path to add a new employee
    path('new/', views.employee_new, name='employee_new'), # Add the employee_new path
    # Path to create a new employee
    path('create/', views.employee_create, name='employee_create'), # Add the employee_create path
    # Edit employee
    path('<int:pk>/edit/', views.employee_edit, name='employee_edit'), # Add the employee_edit path
    # Update employee
    path('<int:pk>/update/', views.employee_update, name='employee_update'), # Add the employee_update path
    # Delete employee
    path('<int:pk>/delete/', views.employee_delete, name='employee_delete'), # Add the employee_delete path
   

]