
from django.http import HttpResponse
from django.shortcuts import render

# Import the Employee model
from employees.models import Employee



def home(request):

    # Get all the employees from the database
    employees=Employee.objects.all()
    # create a dictionary to hold the employees data
    context = {
        'employees':employees,
    }

    # Render the home.html template with the employees data
    return render(request, 'home.html', context)