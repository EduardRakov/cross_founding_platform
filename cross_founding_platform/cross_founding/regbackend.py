from django.dispatch import receiver

from cross_founding_platform.cross_founding.forms import BackerRegistrationForm
from cross_founding_platform.cross_founding.models import Backer

from registration.signals import user_registered

@receiver(user_registered)
def user_created(sender, user, request, **kwargs):
    form = BackerRegistrationForm(request.POST)
    user.first_name = form.data["first_name"]
    user.last_name = form.data["last_name"]
    user.save()

    extra_data = Backer(user=user)
    extra_data.gender = form.data["gender"]
    extra_data.location = request.META['REMOTE_ADDR']
    extra_data.dob_at = form.data["year_dob"] + "-" + form.data["month_dob"] + "-" + form.data["day_dob"]
    extra_data.save()

user_registered.connect(user_created)