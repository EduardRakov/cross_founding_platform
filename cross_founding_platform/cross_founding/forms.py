from django import forms
from django.utils.translation import ugettext_lazy as _

from registration.forms import RegistrationFormUniqueEmail

from cross_founding_platform.cross_founding.models import Backer, Profession

attrs_dict = {'class': 'styled-select'}

PROFESSION_CHOICES = [(profession.id, profession.name) for profession in Profession.objects.all()]

class BackerRegistrationForm(RegistrationFormUniqueEmail):
    def __init__(self, *args, **kwargs):
        super(BackerRegistrationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    email = forms.EmailField(label=_('Email'), error_messages={'required': _('Input your email address')})
    first_name = forms.CharField(max_length=30, required=True, label=_('First Name'),
        error_messages={'required': _('Input your first name')})
    last_name = forms.CharField(max_length=30, required=True, label=_('Last Name'),
        error_messages={'required': _('Input your last name')})
    gender = forms.ChoiceField(widget=forms.Select(attrs=attrs_dict), choices=Backer.GENDER,
        label=_('Gender'), error_messages={'required': _('Select your gender')})
    dob_at = forms.DateField(label=_('Date of birth'), error_messages={'required': _('Date of birth is required field')})
    profession = forms.ChoiceField(label=_('Profession'), choices=PROFESSION_CHOICES,
        widget=forms.Select(attrs=attrs_dict), required=False,
        error_messages={'required': _('Choose your profession')})