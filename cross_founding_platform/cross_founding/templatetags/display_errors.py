from django import template

register = template.Library()

@register.filter(name='display_errors')
def display_errors_except(BackerRegistrationForm, args):

    template_args = args.split(', ')
    errors = ''

    for error_key in BackerRegistrationForm.errors.keys():
        if error_key not in template_args:
            errors += str(BackerRegistrationForm.errors[error_key])
    return errors

