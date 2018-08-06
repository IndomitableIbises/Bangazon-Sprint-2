# Author: Raf
from django.db import models


class Department(models.Model):
    dept_name = models.CharField(default="", max_length=30)

    class Meta:
        db_table = "department"

    def __str__(self):
        return self.dept_name