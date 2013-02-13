from twisted.test.test_amp import tempSelfSigned
from django.db import models
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from registration.models import RegistrationManager

from south.modelsinspector import add_introspection_rules

from model_utils import Choices

from cross_founding_platform.cross_founding.fields import AutoOneToOneField

add_introspection_rules([], ["^cross_founding_platform\.cross_founding\.fields\.AutoOneToOneField"])

class Backer(models.Model):
    GENDER = Choices(
        (1, 'Unspecified', _('Unspecified')),
        (2, 'Male', _('Male')),
        (3, 'Female', _('Female')),
    )

    PROFESSION = Choices(
        (1, 'Unspecified', _('Unspecified')),
        (2, 'Business_Analyst', _('Business Analyst')),
        (3, 'QA_Engineer', _('QA Engineer')),
        (4, 'PR_Manager', _('PR-Manager')),
    )
    user = AutoOneToOneField(User, primary_key=True)

    gender = models.IntegerField(_('Gender'), max_length=1, choices=GENDER, default=GENDER.Unspecified)
    dob_at = models.DateField(_('Date of birth'))
    profession = models.IntegerField(_('Profession'), max_length=1, choices=PROFESSION, default=PROFESSION.Unspecified)
    location = models.CharField(max_length=16)
    twitter_user = models.BooleanField(_('twitter user'), default=False,
        help_text=_('This user was registered via twitter'))
    facebook_user = models.BooleanField(_('facebook user'), default=False,
        help_text=_('This user was registered via facebook'))
    third_party_id = models.BigIntegerField(blank=True, unique=True, null=True, default=None)
    access_token = models.TextField(blank=True, null=True)
    expire_token = models.IntegerField(blank=True, null=True)
    secret_token = models.TextField(blank=True, null=True)

    def disconnect_facebook(self):
        self.access_token = None
        self.facebook_id = None

    def clear_access_token(self):
        self.access_token = None
        self.save()
    def __unicode__(self):
        return u'%s' % self.user

    def disconnect_facebook(self):
        self.access_token = None
        self.twitter_id = None

    def clear_access_token(self):
        self.access_token = None
        self.save()

    class Meta:
        db_table = u'backers'