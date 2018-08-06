#Author: Erin Agobert
from django.db import models


class Computer(models.Model):
    """ Model represents employee computers"""
    name = models.CharField(max_length=30)
    purchase_date = models.DateField()
    decom_date = models.DateField()
    employee = models.ForeignKey(
        'Employee',
        on_delete = models.CASCADE
    )

    class Meta:
        db_table = "computer"

    def __str__(self):
        return self.name
