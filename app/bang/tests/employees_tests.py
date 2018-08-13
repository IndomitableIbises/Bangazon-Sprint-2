# Author: Hayley
import unittest
from django.test import TestCase
from django.urls import reverse
from bang.models import Employees


"""
This has all tests for Employees:
    -Employees List test
    -Employees Form Test
    -Employees Post Test
"""

class EmployeesTest(TestCase):

    def test_list_employees(self):
        new_employee_1 = Employees.objects.create(
            first_name = 'fred',
            last_name = 'landsberg',
            start_date = '2008-10-09',
            department = '1' 
        ),
        new_employees_2 = Employees.objects.create(
            first_name = 'jackson',
            last_name = 'smith',
            start_date = '2009-10-04',
            department = '1' 
        )

        # Issue a GET request.
        # 'reverse' is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
        response = self.client.get(reverse('bang:employees'))
        #self.client acts like requester

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 1 DEPARTMENT.
        # The key 'department_list' comes from the departmentViewModel where we said context_object_name = 'department_list'
        self.assertEqual(len(response.context['employees_list']), 1)

        # Is this stuff in the content of the body?
        # .encode converts from unicode to utf-8
        # example:
        # If the string is: pythön!
        # The encoded version is: b'pyth\xc3\xb6n!'
        self.assertIn(new_employee_1.first_name.encode(), response.content)

    def test_get_employees_form(self):

      response = self.client.get(reverse('bang:employees_form'))

      self.assertIn(
          '<form'.encode(), response.content)

    def test_post_employees(self):

      response = self.client.post(reverse('bang:employees_form'), {'first_name': 'hayley'})

      # Getting 200 back because we have a success url and the view is redirecting under the covers?
      self.assertEqual(response.status_code, 200)

#       Your test suite must verify that the response has an employees collection in the context.

#   * Your test suite must verify that the correct template was used to render the response.

#   * Your test suite must verify that the content of the response has one, or more, of the values that are expected. For example, if one of the employees in Fred Jackson, then your test must test that both "Fred" and "Jackson" are in the response content. Likewise for the department.

# * Your test suite must verify that the content of the response has all of the required input fields.

#   * Your test suite must verify that the response has a department collection in the context in order for the drop down to be populated.

#   * Your test suite must verify that the content of the response has all of the expected values of the employee - name, department, computer, and training programs.

#   * Your test suite must verify that the response has an employee object in the context.

#  * Your test suite must verify that the content of the response has all of the required input fields.

#   * Your test suite must verify that the response has an employee collection in the context, and contains all of the properties needed for populating the form.