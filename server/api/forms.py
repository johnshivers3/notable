from django.forms import ModelForm, widgets
from .models import Doctor, Appt_Data


class Doctor(ModelForm):
    class Meta:
        model = Doctor
        fields = ["first_name", "last_name", "email"]


class ApptForm(ModelForm):
    class Meta:
        model = Appt_Data
        fields = ["phys_id", "first_name", "last_name", "date", "time", "kind"]
