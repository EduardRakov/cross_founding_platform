from django.forms import ModelForm, RegexField, PasswordInput, TextInput
#from registration.forms import TextInput
from registration.forms import RegistrationForm, RegistrationFormUniqueEmail
from registration.models import RegistrationProfile
import site
from cross_founding_platform.cross_founding.models import Backer
from django.contrib.auth.models import User
from django.contrib.sites.models import Site, RequestSite
from registration import signals
from registration.models import RegistrationProfile
from django import forms
#
#class BackerForm(ModelForm):
#    class Meta:
#        model = Backer
#
#    username = RegexField(
#        label="USERNAME",
#        required=True,
#        max_length=30,
#        min_length=4,
#        regex=r'^([a-zA-Z])+$',
#        error_messages={"invalid": "Letters only"}
#    )
#
#    first_name = RegexField(
#        label="FIRST NAME",
#        required=True,
#        widget = TextInput(attrs={'style':'color:red'}),
#        max_length=30,
#        min_length=2,
#        regex=r'^([a-zA-Z])+$',
#        error_messages={"invalid": "Letters only"}
#    )
#
#    last_name = RegexField(
#        label="LAST NAME",
#        required=True,
#        max_length=30,
#        min_length=2,
#        regex=r'^([a-zA-Z])+$',
#        error_messages={"invalid": "Letters only"}
#    )

    # email = RegexField(
    # label="EMAIL",
    # required=True
    # )
#    password = RegexField(
#        label="PASSWORD",
#        required=True,
#        widget = PasswordInput,
#        max_length=25,
#        min_length=6,
#        regex=r'^([a-zA-Z\w@,./\\:+*-])+$',
#        error_messages={"invalid": "Letters only"}
#    )

    # gender = RegexField(
    # label="GENDER",
    # widget=ModelChoiceField()
    # )
    # dob_at = RegexField(
    # label="DATE OF BIRTH",
    # required=True
    # )
#RegistrationForm.base_fields.update(BackerForm.base_fields)
def save(self, user):
    try:
        data = user.get_profile()

    except:
        data = Backer(user=user)

    data.first_name = self.cleaned_data["first_name"]
    data.save()

class BackerRegistrationForm(RegistrationFormUniqueEmail):

    first_name = forms.CharField(label='first name')

#    def save(self, request, profile_callback=None, **kwargs):
#        user = super(BackerRegistrationForm, self).save(profile_callback=None)
#        backer = Backer.objects.get_or_create(
#            user=user,
#            firts_name=self.cleaned_data['first_name'],
#            last_name=self.cleaned_data['last_name']
#
#        )
#        username, email, password = kwargs['username'], kwargs['email'], kwargs['password1']
#        new_user = RegistrationProfile.objects.create_inactive_user(username, email,
#            password, site)
#        signals.user_registered.send(sender=self.__class__,
#            user=new_user,
#            request=request)
#        u = User.objects.get(username=new_user.username)
#        u.first_name = kwargs['first_name']
#        u.last_name = kwargs['last_name']
#        u.save()
#
#        return new_user