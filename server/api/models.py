from django.utils.timezone import now
from django.db import models

# Create your models
class Record(models.Model):
    record_name = models.CharField(max_length=255)
    record_date = models.DateTimeField("date recorded", auto_now=True)

    def __str__(self):
        return "%s %s" % (self.record_name, self.record_date)


class Record_Data(models.Model):
    record_id = models.ForeignKey(Record, on_delete=models.CASCADE)
    data_text = models.TextField(max_length=255)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return "%s %s %s" % (self.record_id, self.data_text, self.priority)
