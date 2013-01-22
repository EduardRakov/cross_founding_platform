from django import forms
from django.utils.translation import ugettext_lazy as _

import datetime

from registration.forms import RegistrationFormUniqueEmail

from cross_founding_platform.cross_founding.models import Backer, Profession

attrs_dict = {'class': 'styled-select'}

PROFESSION_CHOICES = [(profession.id, profession.name) for profession in Profession.objects.all()]

class BackerRegistrationForm(RegistrationFormUniqueEmail):
    def __init__(self, *args, **kwargs):
        super(BackerRegistrationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    email = forms.EmailField(widget=forms.TextInput(attrs=dict({'class': 'required'}, maxlength=75)),
        label=_("E-mail"), error_messages={'required': _('Input your email address')})

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'required'}, render_value=False),
        label=_("Password"), error_messages={'required': _('Input your password')})

    first_name = forms.RegexField(
        regex=r'^([a-zA-Z])+$',
        widget=forms.TextInput,
        max_length=30,
        min_length=2,
        label=_('First Name'),
        error_messages={'required': _('Input your first name'), 'invalid': _('First name must be letters only')}
    )

    last_name = forms.RegexField(
        regex=r'^([a-zA-Z])+$',
        widget=forms.TextInput,
        max_length=30,
        min_length=2,
        label=_('Last Name'),
        error_messages={'required': _('Input your last name'), 'invalid': _('Last name must be letters only')}
    )

    dob_at = forms.DateField(
        required=False,
        label=_('Date of birth'),
        error_messages={'required': _('Date of birth is required field')})

    month_dob = forms.CharField(label=_('Month'),
        widget=forms.TextInput(attrs={'placeholder': 'MM', 'class': 'input-block-new-day-level'}))
    day_dob = forms.CharField(label=_('Day'),
        widget=forms.TextInput(attrs={'placeholder': 'DD', 'class': 'input-block-new-day-level'}))
    year_dob = forms.CharField(label=_('Year'),
        widget=forms.TextInput(attrs={'placeholder': 'YYYY', 'class': 'input-block-new-year-level'}))

    gender = forms.ChoiceField(
        widget=forms.Select(attrs=attrs_dict),
        choices=Backer.GENDER,
        label=_('Gender'),
        error_messages={'required': _('Select your gender')}
    )

    profession = forms.ModelChoiceField(
        queryset=Profession.objects.all(),
        required=False,
        label=_('Profession (optional)'),
        widget=forms.Select(attrs=attrs_dict)
    )

    def clean_dob_at(self):
        try:
            dob_at = datetime.date(int(self.data["year_dob"]), int(self.data["month_dob"]), int(self.data["day_dob"]))
        except:
            raise forms.ValidationError('Please input valid date')

        return dob_at