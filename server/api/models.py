from django.db import models

# Create your models
class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()



class Appt_Data(models.Model):
    phys_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    kind = models.CharField(max_length=255)
