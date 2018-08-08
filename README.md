# Bangazon-Sprint-2


## Installation

### Requirements
1. Python3
1. SQLite3
1. Django
1. [OPTIONAL: to seed the database using faker use [This Link](https://github.com/nashville-software-school/bangazon-llc/blob/ef4cb16ed7fb5ee5141a58cfbece67a7fdf8e673/DB_RESET_SEED_SYSTEM.md "Seeder Instructions")]

### PIP dependencies for this app
1. django
1. django_seed (if you intend to seed the database for testing)

### Steps
1. download or clone the repository
1. [OPTIONAL: if you would like to seed the database with dummy data from the 'app' directory run `django_data.sh bang faker_factory`]
1. to run the server cd into the 'app' directory and run `python manage.py runserver`
1. Visit the [localhost page](http://127.0.0.1:8000/bang/ "Default Django local URL") specified by the terminal
+ [*NOTE*: windows gitbash users will need to add the django_data to the root app directory and use `./django_data.sh bang faker_factory`] 
