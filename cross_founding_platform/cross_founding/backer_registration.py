from django.dispatch import receiver

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
    backer.dob_at = '2011-11-11' #form.date_of_birth
    backer.save()

user_registered.connect(backer_registration)