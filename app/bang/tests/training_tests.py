import unittest
from django.test import TestCase
from django.urls import reverse
from bang.models import Training

#Sean Irwin
class TrainingTest(TestCase):

    def test_list_training(self):
        new_training = Training.objects.create(
            name = "asdf",
            description = "stuff and things",
            start_date = "2012-12-12",
            end_date = "2012-12-12",
            max_attendees = "12"
        )

        newer_training = Training.objects.create(
            name = "asdff",
            description = "stuff and things",
            start_date = "2020-12-12",
            end_date = "2020-12-12",
            max_attendees = "12"
        )

        # Issue a GET request.
        # 'reverse' is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
        response = self.client.get(reverse('bang:training'))
        #self.client acts like requester

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 1 training.
        # The key 'training_list' comes from the trainingViewModel where we said context_object_name = 'training_list'
        self.assertEqual(len(response.context['training_list']), 2)


        # Is this stuff in the content of the body?
        # .encode converts from unicode to utf-8
        # example:
        # If the string is: pythön!
        # The encoded version is: b'pyth\xc3\xb6n!'


    #    context - training_details and training_delete
