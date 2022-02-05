from django.db import models

# Create your models h
class Record(models.Model):
    record_name = models.CharField(max_length=255)
    record_date = models.DateTimeField("date recorded")

    def __str__(self):
        return self.record_name

class Record_Data(models.Model):
    record_id = models.ForeignKey(Record, on_delete=models.CASCADE)
    data_text = models.CharField(max_length=255)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.data_text
