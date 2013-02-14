from django.dispatch import receiver

from registration.signals import user_registered

from cross_founding_platform.cross_founding.forms import BackerRegistrationForm
from cross_founding_platform.cross_founding.models import Backer

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
    backer.twitter_user = form.data['twitter_user']
    backer.facebook_user = form.data['facebook_user']
    backer.access_token = form.data['access_token']if form.data['access_token'] != '' else None
    backer.secret_token = form.data['secret_token']if form.data['secret_token'] != '' else None
    backer.expire_token = form.data['expire_token']if form.data['expire_token'] != '' else None
    backer.third_party_id = form.data['third_party_id']if form.data['third_party_id'] != '' else None
    backer.save()

user_registered.connect(backer_registration)