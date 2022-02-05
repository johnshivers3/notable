from django.contrib import admin

# Register your models here.
from .models import Record, Record_Data

admin.site.register(Record)
admin.site.register(Record_Data)
