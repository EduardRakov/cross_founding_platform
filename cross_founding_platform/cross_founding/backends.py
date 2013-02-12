from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User

from cross_founding_platform.cross_founding.models import Backer

class ThirdPartyBackend(object):

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