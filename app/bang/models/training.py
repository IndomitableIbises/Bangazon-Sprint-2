#Sean Irwin
from django.db import models


class Training(models.Model):
    name = models.CharField(default="", max_length=30)
    description = models.CharField(default="", max_length=100)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    max_attendees = models.IntegerField(default=1)


    class Meta:
        db_table = "training"

    def __str__(self):
        return self.name