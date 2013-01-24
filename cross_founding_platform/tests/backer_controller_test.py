from unittest import TestCase
from django.contrib.auth.models import User
from django.test import Client

#print >> sys.stderr, self.get_empty_form()
#import sys
from cross_founding_platform.cross_founding.models import Backer

class BackerRegistrationCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_should_validation_backer_form_without_data(self):
        response = self.client.post('/accounts/register/', self.get_empty_form())

        self.assertEqual(response.status_code, 200)

        for i in self.get_form_fields():
            errors = response.context['form'][i].errors
            self.assertTrue((len(errors) == 1 and len(errors[0]) > 0), "Should return an error for %s field" % i)

    def test_should_validation_backer_form_with_data(self):
        data = {'username': 'joedoe', 'email': 'joe@example.com', 'password1': 'secret', 'first_name': 'Joe',
                'last_name': 'Doe', 'year_dob': '1990', 'month_dob': '01', 'day_dob': '01', 'gender': '1'}

        response = self.client.post('/accounts/register/', data)
        self.assertEqual(response.request['REQUEST_METHOD'], 'POST')

#        self.user = User.objects.get(pk=1)
#        self.backer = self.user.get_profile()

#        self.assertEqual(self.user.username, "joedoe")
#        self.assertEqual(self.user.first_name, "Joe")
#        self.assertEqual(self.user.last_name, "Doe")
#        self.assertEqual(self.user.email, "joe@example.com")
#        self.assertEqual(self.user.password, "secret")
#        self.assertEqual(self.backer.gender, 1)
#        self.assertEqual(self.backer.location, "127.0.0.1")

    def get_form_fields(self):
        return ['username', 'email', 'password1', 'first_name', 'last_name', 'year_dob', 'month_dob', 'day_dob',
                'gender']

    def get_empty_form(self):
        return dict.fromkeys(self.get_form_fields(), '')