from django.contrib import admin
from .models import Module, Course, Registration
# Register your models here.

admin.site.register(Module)

admin.site.register(Course)

admin.site.register(Registration)