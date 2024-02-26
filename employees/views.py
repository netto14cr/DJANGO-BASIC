
from django.shortcuts import render,redirect, get_object_or_404
from employees.models import Employee


# Create the employee_detail view
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    # create a dictionary to pass to the template
    context = {
        'employee': employee,
    }
    return render(request, 'employee_detail.html', context)


# Create the employee_new view
def employee_new(request):
    return render(request, 'employee_new.html', {})


def employee_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        photo = request.FILES.get('photo')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            photo=photo,
            designation=designation,
            email=email,
            phone_number=phone_number
        )

        return redirect('home')  # redirect to the list of employees after creation

    return render(request, 'employee_new.html')



# Edit employee
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        photo = request.FILES.get('photo')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        employee.first_name = first_name
        employee.last_name = last_name
        employee.photo = photo
        employee.designation = designation
        employee.email = email
        employee.phone_number = phone_number
        employee.save()

        return redirect('employee_detail', pk=pk)  # redirect to the employee detail page after editing

    context = {
        'employee': employee,
    }
    return render(request, 'employee_edit.html', context)



# Update employee
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        photo = request.FILES.get('photo')
        designation = request.POST.get('designation')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')

        employee.first_name = first_name
        employee.last_name = last_name
        employee.photo = photo
        employee.designation = designation
        employee.email = email
        employee.phone_number = phone_number
        employee.save()

        return redirect('employee_detail', pk=pk)  # redirect to the employee detail page after updating

    context = {
        'employee': employee,
    }
    return render(request, 'employee_detail.html', context)


# Delete employee
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('home')  # redirect to the list of employees after deletion

    context = {
        'employee': employee,
    }
    return render(request, 'employee_delete.html', context)