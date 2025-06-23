from django.contrib import admin

# Register your models here.

from .models import Record

admin.site.register(Record)  # Register the Record model with the admin site