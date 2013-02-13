from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site, RequestSite

from registration import signals
from registration.backends.default import DefaultBackend
from registration.models import RegistrationProfile

from cross_founding_platform.cross_founding.models import Backer

class ThirdPartyRegisterBackend(DefaultBackend):
    def register(self, request, **kwargs):
        username, email, password = kwargs['username'], kwargs['email'], kwargs['password1']

        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        new_user = RegistrationProfile.objects.create_inactive_user(username, email,
            password, site,
            send_email=False)
        new_user.is_active = True
        new_user.save()

        signals.user_registered.send(sender=self.__class__,
            user=new_user,
            request=request)
        return new_user

    def post_registration_redirect(self, request, user):

        return 'profile', (), {}

class ThirdPartyAuthBackend(object):

    def authenticate(self, token=None, third_party_id=None):
        try:
            backer = Backer.objects.get(third_party_id=third_party_id, access_token=token)
            user = User.objects.get(pk=backer.user_id)
            user.is_active=True
            user.save()

            return user

        except Backer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except auth_models.User.DoesNotExist:
            return None