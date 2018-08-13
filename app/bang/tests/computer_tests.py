# Author: Erin
import unittest
from django.test import TestCase
from django.urls import reverse
from bang.models import Computer


class ComputerTest(TestCase):

    def test_computer_response(self):
        """ Test verifies response content contains all required input fields """
        
        Computer.objects.create(
            make = 'Apple',
            model = 'MacBook Pro',
            purchase_date = '2018-08-08'
        )

        response = self.client.get(reverse('bang:computer_list'))

        # Check that response includes all fields
        self.assertContains(response, 'Apple', count=None, status_code=200)
        self.assertContains(response, 'MacBook Pro', count=None, status_code=200)

        #Note:  standard date formats are converted from YYYY-MM-DD to Mon. DD, YYYY
        self.assertContains(response, 'Aug. 8, 2018', count=None, status_code=200)

    def test_post_new_computer(self):
        """ Test verifies client can post a new computer using computer_form and redirects to success url """

        response = self.client.post(reverse('bang:computer_form'), {
            'make': 'Apple',
            'model': 'MacBook',
            'purchase_date': '2018-08-09'
            }, follow=True)
        
        #Asserts response has posted and redirected successfully to success url
        self.assertEqual(response.status_code, 200)

    def test_delete_computer(self):
        """ Test verifies client can delete a computer using computer_form and redirects to success url """

        #This posts a computer to the client
        response1 = self.client.post(reverse('bang:computer_form'), {
            'make': 'Apple',
            'model': 'MacBook',
            'purchase_date': '2018-08-09'
            }, follow=True)

        response2 = self.client.get('/bang/computers/1/computer_delete/',)

        response3 = self.client.delete('/bang/computers/1', follow=True)
        
        #Asserts response1 has posted and redirected successfully to success url
        self.assertEqual(response1.status_code, 200)

        #Asserts response2 contains the valid template response for a computer with no employee assigned
        self.assertContains(response2, 'Are you sure you want to delete', count=None, status_code=200)

        #Asserts response 2 is using the correct template
        self.assertTemplateUsed(response=response2, template_name='bang/computer_confirm_delete.html')

        #Asserts response3 has deleted
        self.assertEqual(response3.status_code, 200)
