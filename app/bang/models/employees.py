from django.db import models
from .department import Department

class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_date = models.DateField()
    supervisor = models.BooleanField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employees'
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
