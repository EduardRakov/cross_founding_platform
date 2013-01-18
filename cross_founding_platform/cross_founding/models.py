from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from model_utils import Choices

from cross_founding_platform.cross_founding.fields import AutoOneToOneField

class Profession(models.Model):
    name = models.CharField(_('Profession'), max_length=15)

    def __unicode__(self):
        return self.name

class Backer(models.Model):

    GENDER = Choices(
        (1, 'Male', _('Male')),
        (2, 'Female', _('Female')),
        (3, 'Unspecified', _('Unspecified'))
    )

    user = AutoOneToOneField(User)

    gender = models.IntegerField(_('Gender'), max_length=1, choices=GENDER, default=GENDER.Unspecified)
    dob_at = models.DateField(_('Date of birth'))
    profession = models.ForeignKey(Profession, blank=True, null=True)
    location = models.CharField(max_length=16, default='127.0.0.1')