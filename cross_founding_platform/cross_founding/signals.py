from django.contrib import auth

from registration.signals import user_activated, user_registered

from cross_founding_platform.cross_founding.forms import BackerRegistrationForm
from cross_founding_platform.cross_founding.models import Backer

def user_created(sender, user, request, **kwargs):
    form = BackerRegistrationForm(request.POST)
    backer = Backer(user=user, first_name=str(form.data['first_name']))
    backer.save()

#def login_on_activation(sender, user, request, **kwargs):
#    user.backend = 'django.contrib.auth.backends.ModelBackend'
#    auth.login(request, user)
#
#    user_activated.connect(login_on_activation)
#    user_registered.connect(user_created)
