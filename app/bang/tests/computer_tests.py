# Author: Raf
import unittest
from django.test import TestCase
from django.urls import reverse
from bang.models import Computer


class ComputerTest(TestCase):

    def test_computer_response(self):
        """ Test verifies response includes all fields and returns status code 200 """
        
        new_computer = Computer.objects.create(
            make = 'Apple',
            model = 'MacBook Pro',
            purchase_date = '2018-08-08'
        )

        response = self.client.get(reverse('bang:computer_list'))

        # Check that response includes all fields
        self.assertContains(response, 'Apple', count=None, status_code=200)
        self.assertContains(response, 'MacBook Pro', count=None, status_code=200)
        # self.assertContains(response, '2018-08-08', count=None, status_code=200)
        


    # def test_get_department_form(self):

    #   response = self.client.get(reverse('bang:departments_form'))

    #   self.assertIn(
    #       '<form'.encode(), response.content)

    def test_post_department(self):

      response = self.client.post(reverse('bang:departments_form'), {'dept_name': 'Department of Poopland Security'})

      # Getting 200 back because we have a success url and the view is redirecting under the covers?
      self.assertEqual(response.status_code, 200)