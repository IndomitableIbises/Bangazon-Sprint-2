from django.core.management.base import BaseCommand
from django_seed import Seed
seeder = Seed.seeder()
import random
from bang.models import Department, Employees, Computer, Training

class Command(BaseCommand):

  def handle(self, *args, **options):
    seeder.add_entity(Department, 5) # the number argument is the total num of rows you want created
    seeder.add_entity(Computer, 25)
    seeder.add_entity(Employees, 25)
    # Override the seeder "guess" of what faker provider you want it to use
    seeder.add_entity(Training, 20)

    inserted_pks = seeder.execute()
