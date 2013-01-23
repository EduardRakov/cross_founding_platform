from django import template

from cross_founding_platform.cross_founding.forms import BackerRegistrationForm

register = template.Library()

def exclude_errors(self, *args):
    try:
        for error in args:
            del self[error]
    except:
        pass
    return self

@register.filter(name='display_errors')
def display_errors(BackerRegistrationForm):
    exclude_errors(BackerRegistrationForm.errors, 'month_dob', 'day_dob', 'year_dob')
    return BackerRegistrationForm.errors


