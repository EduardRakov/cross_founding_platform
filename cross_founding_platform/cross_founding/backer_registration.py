from django.dispatch import receiver
from django.db.models import signals

from django.contrib.auth.models import User

from cross_founding_platform.cross_founding.forms import BackerRegistrationForm
from cross_founding_platform.cross_founding.models import Backer

from registration.signals import user_registered

#@receiver(user_registered)
#def backer_registration(sender, user, request, **kwargs):
#    form = BackerRegistrationForm(request.POST)
#    print form._errors
#
#    user.first_name = form.cleaned_data["first_name"]
#    user.last_name = form.cleaned_data["last_name"]
#    user.save()
#
#    backer = Backer(user=user)
#    backer.gender = form.cleaned_data["gender"]
#    backer.location = request.META['REMOTE_ADDR']
#    backer.dob_at = form.cleaned_data['dob_date']
#    backer.save()
#
#user_registered.connect(backer_registration)
#
#def create_profile(sender, **kwargs):
#    user = kwargs["instance"]
#
#    if kwargs["created"]:
#        user_profile = Backer(user=user)
#        user_profile.save()
#
#signals.post_save.connect(create_profile, sender=User)