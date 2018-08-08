# Author: Raf
import unittest
from django.test import TestCase
from django.urls import reverse
from bang.models import Department


class DepartmentTest(TestCase):

    def test_list_department(self):
        new_department = Department.objects.create(
            dept_name = "Test Department"
        )

        # Issue a GET request.
        # 'reverse' is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
        response = self.client.get(reverse('bang:departments'))
        #self.client acts like requester

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 1 DEPARTMENT.
        # The key 'department_list' comes from the departmentViewModel where we said context_object_name = 'department_list'
        self.assertEqual(len(response.context['department_list']), 1)

        # Is this stuff in the content of the body?
        # .encode converts from unicode to utf-8
        # example:
        # If the string is: pythön!
        # The encoded version is: b'pyth\xc3\xb6n!'
        self.assertIn(new_department.dept_name.encode(), response.content)

    def test_get_department_form(self):

      response = self.client.get(reverse('bang:departments_form'))

      self.assertIn(
          '<input type="text" dept_name="name" maxlength="100" required id="id_dept_name" />'.encode(), response.content)

    def test_post_department(self):

      response = self.client.post(reverse('bang:departments_form'), {'dept_name': 'Department of Poopland Security'})

      # Getting 301 back because we have a success url and the view is redirecting under the covers?
      self.assertEqual(response.status_code, 301)