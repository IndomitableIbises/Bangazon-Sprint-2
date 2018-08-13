# Author: Raf
from django.db import models


'''
Department Model

Model for Departments include the following:
    dept_name is a string defaulted to ""
'''


class Department(models.Model):
    dept_name = models.CharField(default="", max_length=30)

    class Meta:
        db_table = "department"

    def __str__(self):
        return self.dept_name