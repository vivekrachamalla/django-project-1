from django.contrib import admin
from .models import *

# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "id"]
