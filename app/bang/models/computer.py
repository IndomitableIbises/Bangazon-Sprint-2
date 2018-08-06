from django.db import models


class Computer(models.Model):
    purchase_date = models.DateField()
    decom_date = models.DateField()
    employee = models.ForeignKey(
        'Employee',
        on_delete = models.CASCADE
    )
