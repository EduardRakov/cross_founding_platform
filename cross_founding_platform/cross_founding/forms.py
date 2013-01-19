from django import forms
from django.forms import ModelForm, RegexField, ModelChoiceField
from django.utils.translation import ugettext_lazy as _

from registration.forms import RegistrationFormUniqueEmail

from cross_founding_platform.cross_founding.models import Backer, Profession

attrs_dict = {'class': 'styled-select'}

PROFESSION_CHOICES = [(profession.id, profession.name) for profession in Profession.objects.all()]

class BackerForm(ModelForm):
    class Meta:
        model = Backer
        fields = ('gender', 'dob_at', 'profession')

    first_name = RegexField(
        label=_('First name'),
        required=True,
        max_length=30,
        min_length=2,
        regex=r'^([a-zA-Z])+$',
        error_messages={'required': _('Input your first name'), 'invalid': _('First name must be letters only')}
    )

    last_name = RegexField(
        label=_('Last name'),
        required=True,
        max_length=30,
        min_length=2,
        regex=r'^([a-zA-Z])+$',
        error_messages={'required': _('Input your last name'), 'invalid': _('Last name must be letters only')}
    )

    dob_at = RegexField(
        label=_('Date of birth'),
        required=True,
        regex=r'^([0-9-])+$',
        error_messages={'required': _('Date of birth is required field'), 'invalid': _('Please input correct date')}
    )

RegistrationFormUniqueEmail.base_fields.update(BackerForm.base_fields)

class BackerRegistrationForm(RegistrationFormUniqueEmail):

    def __init__(self, *args, **kwargs):
        super(BackerRegistrationForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    email = forms.EmailField(widget=forms.TextInput(attrs=dict({'class': 'required'}, maxlength=75)),
        label=_("E-mail"), error_messages={'required': _('Input your email address')})

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'required'}, render_value=False),
        label=_("Password"),  error_messages={'required': _('Input your password')})

#    profession = forms.ChoiceField(label=_('Profession'), choices=PROFESSION_CHOICES,
#        widget=forms.Select(attrs=attrs_dict), required=False,
#        error_messages={'required': _('Choose your profession')})