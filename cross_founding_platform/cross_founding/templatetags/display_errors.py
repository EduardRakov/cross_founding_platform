from django import template
from django.forms.util import ErrorDict
from django.forms.util import ErrorList

from cross_founding_platform.cross_founding.forms import BackerRegistrationForm

register = template.Library()

@register.filter(name='display_errors')
def display_errors_except(BackerRegistrationForm, args):

    try:
        for error in args.split(', '):
            del BackerRegistrationForm.errors[error]
    except:
        pass

    errors = ''
    for n in BackerRegistrationForm.errors.keys():
        errors += str(BackerRegistrationForm.errors[n])
    return errors

