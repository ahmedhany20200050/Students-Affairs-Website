from django.contrib import admin
from .models import Employees, Students

# Register your models here.
admin.site.register(Students)
admin.site.register(Employees)