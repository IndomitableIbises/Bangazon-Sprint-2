from django.db import models
from django.urls import reverse
from .department import Department
from .computer import Computer
from .training import Training

class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_date = models.DateField()
    supervisor = models.BooleanField()
<<<<<<< HEAD
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees_department')
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, blank=True, null=True, related_name='employees_computer')
    trainings = models.ManyToManyField(Training)
=======
    department = models.ForeignKey(Department, on_delete=models.CASCADE,)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE, blank=True, null=True,)
>>>>>>> af989b428e69ff8eef3efa17c3e9ee167f0b1a44

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Author: Raf
    def get_absolute_url(self):
        return reverse("bang:employees_detail", kwargs={"pk": self.pk})
