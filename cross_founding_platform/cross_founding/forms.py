from django import forms
from django.utils.translation import ugettext_lazy as _

import datetime

from registration.forms import RegistrationFormUniqueEmail

from cross_founding_platform.cross_founding.models import Backer, Profession


PROFESSION_CHOICES = [(profession.id, profession.name) for profession in Profession.objects.all()]

class BackerRegistrationForm(RegistrationFormUniqueEmail):
    def __init__(self, *args, **kwargs):
        super(BackerRegistrationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'required', 'tabindex': '1'}),
        label=_("Username"),
        error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})

    email = forms.EmailField(widget=forms.TextInput(attrs=dict({'class': 'required', 'tabindex': '2'}, maxlength=75)),
        label=_("E-mail"), error_messages={'required': _('Input your email address')})

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'required', 'tabindex': '3'}, render_value=False),
        label=_("Password"), error_messages={'required': _('Input your password')})

    first_name = forms.RegexField(
        regex=r'^([a-zA-Z])+$',
        widget=forms.TextInput(attrs={'tabindex': '7'}),
        max_length=30,
        min_length=2,
        label=_('First Name'),
        error_messages={'required': _('Input your first name'), 'invalid': _('First name must be letters only')}
    )

    last_name = forms.RegexField(
        regex=r'^([a-zA-Z])+$',
        widget=forms.TextInput(attrs={'tabindex': '8'}),
        max_length=30,
        min_length=2,
        label=_('Last Name'),
        error_messages={'required': _('Input your last name'), 'invalid': _('Last name must be letters only')}
    )

    dob_at = forms.DateField(
        required=False,
        label=_('Date of birth'),
        error_messages={'required': _('Date of birth is required field')})

    month_dob = forms.CharField(label=_('Month'), max_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'MM', 'class': 'input-block-new-day-level', 'tabindex': '5'}))
    day_dob = forms.CharField(label=_('Day'), max_length=2,
        widget=forms.TextInput(attrs={'placeholder': 'DD', 'class': 'input-block-new-day-level', 'tabindex': '4'}))
    year_dob = forms.CharField(label=_('Year'), max_length=4,
        widget=forms.TextInput(attrs={'placeholder': 'YYYY', 'class': 'input-block-new-year-level', 'tabindex': '6'}))

    gender = forms.ChoiceField(
        widget=forms.Select(attrs= {'class': 'styled-select', 'tabindex': '9'}),
        choices=Backer.GENDER,
        label=_('Gender'),
        error_messages={'required': _('Select your gender')}
    )

    profession = forms.ModelChoiceField(

        queryset=Profession.objects.all(),
        required=False,
        label=_('Profession (optional)'),
        widget=forms.Select(attrs={'class': 'styled-select', 'tabindex': '10'})
    )

    def clean_dob_at(self):
        try:
            dob_at = datetime.date(int(self.data["year_dob"]), int(self.data["month_dob"]), int(self.data["day_dob"]))
        except:
            raise forms.ValidationError('Please input valid date')

        return dob_at