from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

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

        (1, '', _(''))
    )
    user = AutoOneToOneField(User, primary_key=True)

    gender = models.IntegerField(_('Gender'), max_length=1, choices=GENDER, default=GENDER.Unspecified)
    dob_at = models.DateField(_('Date of birth'))
    profession = models.IntegerField(choices=GENDER, default=PROFESSION.Unspecified)
    location = models.CharField(max_length=16)