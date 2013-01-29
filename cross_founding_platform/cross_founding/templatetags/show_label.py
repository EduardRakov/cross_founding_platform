from django import template

register = template.Library()

@register.filter(name='show_label')
def show_label(BackerRegistrationForm, args):
    return args

