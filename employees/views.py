
from django.shortcuts import render, get_object_or_404
from employees.models import Employee


# Create the employee_detail view
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    # create a dictionary to pass to the template
    context = {
        'employee': employee,
    }
    return render(request, 'employee_detail.html', context)



