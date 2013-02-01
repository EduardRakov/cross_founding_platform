from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.dispatch import receiver
from django_facebook import signals
from django_facebook.signals import facebook_user_registered

from cross_founding_platform.cross_founding.forms import BackerRegistrationForm
from cross_founding_platform.cross_founding.models import Backer

from registration.signals import user_registered

@receiver(user_registered)
def backer_registration(sender, user, request, **kwargs):

    form = BackerRegistrationForm(request.POST)

    user.first_name = form.data["first_name"]
    user.last_name = form.data["last_name"]
    user.save()

    backer = Backer(user=user)
    backer.gender = form.data["gender"]
    backer.location = request.META['REMOTE_ADDR']
    backer.dob_at = form.get_dob()
    backer.save()

user_registered.connect(backer_registration)

@receiver(facebook_user_registered)
def fb_user_registered_handler(sender, user, facebook_data, **kwargs):
    user.first_name = facebook_data["first_name"]
    user.last_name = facebook_data["last_name"]
    user.save()

signals.facebook_user_registered.connect(fb_user_registered_handler, sender=User)


