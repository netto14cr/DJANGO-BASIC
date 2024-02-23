
# Configurated URL patterns for the employees app

# Import the include function
from django.urls import path
# import the views module from the employees app
from . import views

urlpatterns = [

    # Path is the primary key of the employee
    path('<int:pk>/', views.employee_detail, name='employee_detail'), # Add the employee_detail path
]