from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django import forms
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
from django.utils.http import int_to_base36
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.hashers import UNUSABLE_PASSWORD
from django.template import loader

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

    month_dob = forms.CharField(label=_('Month'), max_length=2, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'MM', 'class': 'input-block-new-day-level', 'tabindex': '5'}),
        error_messages={'required': _(u'Input month'), 'invalid': _(u'Input valid month'), }
    )

    day_dob = forms.CharField(label=_('Day'), max_length=2, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'DD', 'class': 'input-block-new-day-level', 'tabindex': '4'}),
        error_messages={'required': _(u'Input day'), 'invalid': _(u'Input valid day'), }
    )

    year_dob = forms.RegexField(
        regex=r'^[0-9]+$',
        label=_('Year'),
        max_length=4,
        widget=forms.TextInput(attrs={'placeholder': 'YYYY', 'class': 'input-block-new-year-level', 'tabindex': '6'}),
        error_messages={'required': _(u'Input year'), 'invalid': _(u'Input valid year')}
    )

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

    def clean(self):
        super(RegistrationFormUniqueEmail, self).clean()

        if not self.is_dob_valid():
            self._errors['date_of_birth'] = self.error_class([u'Please, input valid date'])
        else:
            self.cleaned_data['dob_date'] = self.get_dob()

        return self.cleaned_data

    def get_dob(self):
        return datetime.date(int(self.data["year_dob"]), int(self.data["month_dob"]), int(self.data["day_dob"]))

    def is_dob_valid(self):
        try:
            if (datetime.date.today() - self.get_dob()).days > 0:
                return True

        except (KeyError, ValueError):
            return False

    def clean_year_dob(self):
        MIN_YEAR = 1900
        year_dob = self.data['year_dob']

        if int(year_dob) < MIN_YEAR:
            self._errors['date_of_birth'] = self.error_class([u'Please, input valid date'])

        return year_dob


class BackerAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label=_("Username"), max_length=30,
        widget=forms.TextInput(attrs={'class': 'input-block-level'}),
        error_messages={'required': _(u'Input your username')})

    password = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'input-block-level'}),
        error_messages={'required': _(u'Input your password')})

    stay_signed_in = forms.BooleanField(required=False, initial=False,
        widget=forms.CheckboxInput(attrs={'class': 'login-checkbox'}))


class PasswordRecoveryForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_(u'New password'), min_length=6, widget=forms.PasswordInput,
        error_messages={
            'required': _(u'Please enter a new password'),
            'min_length': _(u'Ensure the password is greater than or equal to %(limit_value)s.'),
        })

    new_password2 = forms.CharField(label=_(u'Verify password'), min_length=6,
        widget=forms.PasswordInput, error_messages={
            'required': _(u'Please fill out verify password field'),
            'min_length': _(u'Ensure the password is greater than or equal to %(limit_value)s.'),
        })


class EmailRecoveryForm(forms.Form):
    email = forms.EmailField(label=_(u'Email'), max_length=75)
    error_messages = {
        'required': _(u"Please enter your email"),
        'unknown': _(u"That e-mail address doesn't have an associated user account"),
        'unusable': _(u"The user account associated with this e-mail address cannot reset the password"),
    }

    def clean_email(self):
        email = self.cleaned_data["email"]
        self.users_cache = User.objects.filter(email__iexact=email,
            is_active=True)
        if not len(self.users_cache):
            raise forms.ValidationError(self.error_messages['unknown'])
        if any((user.password == UNUSABLE_PASSWORD)
            for user in self.users_cache):
            raise forms.ValidationError(self.error_messages['unusable'])
        return email

    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None):
        from django.core.mail import send_mail

        for user in self.users_cache:
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            c = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': int_to_base36(user.id),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': use_https and 'https' or 'http',
            }
            subject = loader.render_to_string(subject_template_name, c)
            subject = ''.join(subject.splitlines())
            email = loader.render_to_string(email_template_name, c)
            send_mail(subject, email, from_email, [user.email])
