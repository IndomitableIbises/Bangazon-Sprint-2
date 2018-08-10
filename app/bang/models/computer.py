#Author: Erin Agobert
from django.db import models
from django.urls import reverse


class Computer(models.Model):
    """ Model represents employee computers"""
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    purchase_date = models.DateField()

    class Meta:
        db_table = "computer"

    # def get_absolute_url(self):
    #     return reverse('computer_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.make
