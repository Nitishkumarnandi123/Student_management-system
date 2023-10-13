from django.contrib import admin

import StudentApp
from StudentApp.models import Course, Student

# Register your models here.
admin.site.register(Course)




admin.site.register(Student)