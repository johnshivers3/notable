from django.forms import ModelForm, widgets
from .models import Record, Record_Data

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields=["record_name",]

class RecordDataForm(ModelForm):
    class Meta:
        model = Record_Data
        fields= ["record_id", "data_text"]
