from django.contrib import admin

# Register your models here.
from .models import Doctor, Appt_Data

admin.site.register(Doctor)
admin.site.register(Appt_Data)
