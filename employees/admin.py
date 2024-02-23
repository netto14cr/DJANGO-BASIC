from django.contrib import admin
from .models import Employee # add this line to import the Employee model

admin.site.register(Employee) # add this line to register the Employee model with the admin site
