from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=8, blank=True) # blank=True means this field is optional

    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True means this field will be set to the 
                                                         # current date and time when a new record is created 
                                                         # ** only once instead of every time the record is updated **
    
    updated_at = models.DateTimeField(auto_now=True)    # auto_now=True means this field will be set to the current
                                                        # date and time when a record is updated
    
    
    # The __str__ method is used to display the name of the employee in the admin interface
    def __str__(self):
        return self.first_name + " " + self.last_name

