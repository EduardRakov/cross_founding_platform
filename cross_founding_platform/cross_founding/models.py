from django.db.models import signals
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

    class Meta:
        db_table = u'backers'
