from django import forms
from django.utils.translation import ugettext_lazy as _

import datetime

from registration.forms import RegistrationFormUniqueEmail

from cross_founding_platform.cross_founding.models import Backer

class BackerRegistrationForm(RegistrationFormUniqueEmail):
    def __init__(self, *args, **kwargs):
        super(BackerRegistrationForm, self).__init__(*args, **kwargs)
        self.initial['choices_field_name'] = 'default value'
        del self.fields['password2']

    username = forms.RegexField(regex=r'^[\w.@+-]+$',
        min_length=4,
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'required', 'tabindex': '1'}),
        label=_("Username"),
        error_messages={
            'required': _(u'Input your username'),
            'invalid': _(u'Username may contain only letters, numbers and @/./+/-/_ characters.'),
            'max_length': _(u'Ensure the username is less than or equal to %(limit_value)s.'),
            'min_length': _(u'Ensure the username is greater than or equal to %(limit_value)s.')
        }
    )

    email = forms.EmailField(widget=forms.TextInput(attrs=dict({'class': 'required', 'tabindex': '2'}, maxlength=75)),
        label=_("E-mail"), error_messages={'required': _(u'Input your email address')})

    password1 = forms.CharField(
        min_length=6,
        widget=forms.PasswordInput(attrs={'class': 'required', 'tabindex': '3'}, render_value=False),
        label=_("Password"),
        error_messages={
            'required': _(u'Input your password'),
            'max_length': _(u'Ensure the password is less than or equal to %(limit_value)s.'),
            'min_length': _(u'Ensure the password is greater than or equal to %(limit_value)s.')
        }
    )

    first_name = forms.RegexField(
        regex=r'^([a-zA-Z])+$',
        widget=forms.TextInput(attrs={'tabindex': '7'}),
        max_length=30,
        min_length=2,
        label=_('First Name'),
        error_messages={
            'required': _(u'Input your first name'), 'invalid': _(u'First name must be letters only'),
            'max_length': _(u'Ensure the first name is less than or equal to %(limit_value)s.'),
            'min_length': _(u'Ensure the first name is greater than or equal to %(limit_value)s.')
        }
    )

    last_name = forms.RegexField(
        regex=r'^([a-zA-Z])+$',
        widget=forms.TextInput(attrs={'tabindex': '8'}),
        max_length=30,
        min_length=2,
        label=_('Last Name'),
        error_messages={
            'required': _(u'Input your last name'), 'invalid': _(u'Last name must be letters only'),
            'max_length': _(u'Ensure the last name is less than or equal to %(limit_value)s.'),
            'min_length': _(u'Ensure the last name is greater than or equal to %(limit_value)s.')
        }
    )

#    dob_at = forms.DateField(
#        required=False,
#        label=_('Date of birth'),
#        error_messages={'required': _(u'Date of birth is required field')})

    month_dob = forms.CharField(label=_('Month'), max_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'MM', 'class': 'input-block-new-day-level', 'tabindex': '5'}))

    day_dob = forms.CharField(label=_('Day'), max_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'DD', 'class': 'input-block-new-day-level', 'tabindex': '4'}))

    year_dob = forms.CharField(label=_('Year'), max_length=4,
        widget=forms.TextInput(attrs={'placeholder': 'YYYY', 'class': 'input-block-new-year-level', 'tabindex': '6'}))

    gender = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'styled-select', 'tabindex': '9'}),
        choices=Backer.GENDER,
        label=_('Gender'),
        error_messages={'required': _(u'Select your gender')}
    )

    profession = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'styled-select', 'tabindex': '10'}),
        choices=Backer.PROFESSION,
        required=False,
        label=_('Profession')

    )

    def date_of_birth(self):
        return datetime.date(int(self.cleaned_data["year_dob"]), int(self.cleaned_data["month_dob"]), int(self.cleaned_data["day_dob"]))

#    def clean(self):
#        cleaned_data = super(RegistrationFormUniqueEmail, self).clean()
#        if self.date_of_birth().isoformat != (self.cleaned_data["year_dob"] + self.cleaned_data["month_dob"] +  self.cleaned_data["day_dob"]):
#            self._errors["day_dob"] = self.error_class([_(u'Please enter a valid date')])

#    def clean_dob_at(self):
#        try:
#            dob_at = self.date_of_birth
#        except:
#            raise forms.ValidationError(_(u'Please enter a valid date'))
#        return dob_at

