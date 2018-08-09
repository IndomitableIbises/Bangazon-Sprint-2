#Author: Erin Agobert
from django.db import models


class Computer(models.Model):
    """ Model represents employee computers"""
    make = models.CharField(max_length=30)
    manufacturer = models.CharField(max_length=30)
    purchase_date = models.DateField()

    class Meta:
        db_table = "computer"

    def __str__(self):
        return self.make
