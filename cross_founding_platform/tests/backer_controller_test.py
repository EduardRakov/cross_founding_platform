from unittest import TestCase
from django.test import Client
from registration.signals import user_registered
from cross_founding_platform.cross_founding.forms import BackerRegistrationForm
from cross_founding_platform.cross_founding.models import Backer

class BackerRegistrationCase(TestCase):

    def test_should_validation_backer(self):
        client = Client()
        response = client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

        response = client.post('/accounts/register/', {
            'username': '', 'email': 'joe@example.com','password': 'secret',
            'first_name': 'Joe', 'last_name': 'Doe'}
        )

        self.assertEqual(response.context['form']['username'].errors, [u'Input your username'])

#        form = BackerRegistrationForm(request.POST)
#
#        user.first_name = form.cleaned_data["first_name"]
#        user.last_name = form.cleaned_data["last_name"]
#        user.save()
#
#        backer = Backer(user=user)
#        backer.gender = form.cleaned_data["gender"]
#        backer.location = request.META['REMOTE_ADDR']
#        backer.dob_at = form.date_of_birth
#        backer.save()
#
#    user_registered.connect(test_should_validation_backer)