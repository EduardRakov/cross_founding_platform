from django.forms import ModelForm, RegexField, PasswordInput, ModelChoiceField
from cross_founding_platform.cross_founding import models

class BackerForm(ModelForm):
    class Meta:
        model = models.Backer

    username = RegexField(
        label="USERNAME",
        required=True,
        max_length=30,
        min_length=4,
        regex=r'^([a-zA-Z])+$',
        error_messages={"invalid": "Letters only"}
    )

    first_name = RegexField(
        label="FIRST NAME",
        required=True,
        max_length=30,
        min_length=2,
        regex=r'^([a-zA-Z])+$',
        error_messages={"invalid": "Letters only"}
    )

    last_name = RegexField(
        label="LAST NAME",
        required=True,
        max_length=30,
        min_length=2,
        regex=r'^([a-zA-Z])+$',
        error_messages={"invalid": "Letters only"}
    )

#    email = RegexField(
#        label="EMAIL",
#        required=True
#    )
    password = RegexField(
        label="PASSWORD",
        required=True,
        widget = PasswordInput,
        max_length=25,
        min_length=6,
        regex=r'^([a-zA-Z\w@,./\\:+*-])+$',
        error_messages={"invalid": "Letters only"}
    )

#    gender = RegexField(
#        label="GENDER",
#        widget=ModelChoiceField()
#    )
#    dob_at = RegexField(
#        label="DATE OF BIRTH",
#        required=True
#    )