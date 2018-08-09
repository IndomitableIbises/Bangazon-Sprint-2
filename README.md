# Bangazon-Sprint-2

## About This Repo

This application is intended to manage the internal structure of the fictional Bangazon LLC. It is used for handling the database the stores details of the departments, employees, computers, and training programs available to the organization. It is built using Python, Django, and SQLite3.

## Table of Contents

[Installation](#installation)  
[Tables](#tables)  
[Usage](#usage)  


# Installation

## Requirements
1. Python3
1. SQLite3
1. Django
1. [OPTIONAL: to seed the database using faker use [This Link](https://github.com/nashville-software-school/bangazon-llc/blob/ef4cb16ed7fb5ee5141a58cfbece67a7fdf8e673/DB_RESET_SEED_SYSTEM.md "Seeder Instructions")]

## PIP dependencies for this app
1. django
1. django_seed (if you intend to seed the database for testing)

## Steps
1. download or clone the repository
1. [OPTIONAL: if you would like to seed the database with dummy data from the root 'app' directory run `django_data.sh bang faker_factory`]
1. to run the server cd into the root 'app' directory and run `python manage.py runserver`
1. Visit the [application url/bang](http://127.0.0.1:8000/bang/ "Default Django local URL") specified by the terminal

[*NOTE*: windows gitbash users will need to add the django_data to the root app directory and use `./django_data.sh bang faker_factory`] 

# Tables

## Computers
* make | String
* model | String
* purchase_date | Date formated as 'yyyy-mm-dd'

## Department
* dept_name | String

## Employees
* first_name | String
* last_name | String
* start_date | Date formated as 'yyyy-mm-dd'
* supervisor | Boolean
* department | Foreign Key to department table
* computer | Foreign Key to computer table

## Training
* name | String
* description | String
* start_date | Date formated as 'yyyy-mm-dd'
* end_date | Date formated as 'yyyy-mm-dd'
* max_attendees | Integer
* attendees | Join table wth Employees

# Usage
after opening the [application url/bang](http://127.0.0.1:8000/bang/ "Default Django local URL") to reach the main page of the application, there will be various navigation buttons to reach the different components for each table. From the separate pages users are able to perform the following tasks:

## Computers
1. Create new computers
1. View the list of all computers
1. Delete computers that **have never been assigned to an employee**
1. View the details of each individual computer

## Department
1. Create new departments
1. View the list of all departments
1. View the details of individual departments which should also list all employees in the deparment

## Employees
1. Create new Employees
1. View the list of all employees
1. View the details of individual employees which should also list the computer(s) assigned to the employee
1. Edit the employees last name, assigned computer, enrolled training, and change their department

## Training
1. Create new training programs
1. View the list of all training programs
1. View the details of individual training programs which should also list the employees enrolled in it.
1. Edit the details of a training program that **has yet to begin**
1. Delete training programs that **has yet to begin**
