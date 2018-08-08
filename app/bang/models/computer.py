#Author: Erin Agobert
from django.db import models
from .employees import Employees


class Computer(models.Model):
    """ Model represents employee computers"""
    make = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    purchase_date = models.DateField()
    decom_date = models.DateField(blank=True)
    employee = models.ForeignKey(
        'Employees',
        on_delete = models.CASCADE,
        blank=True
    )

    class Meta:
        db_table = "computer"

    def __str__(self):
        return self.make
