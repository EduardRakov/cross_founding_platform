from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

import registration.backends.default.urls as regUrls

from cross_founding_platform.cross_founding.forms import BackerRegistrationForm, BackerAuthenticationForm

from cross_founding_platform.cross_founding.signals import *

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^accounts/register/$',
        'registration.views.register',
        {'backend': 'registration.backends.default.DefaultBackend', 'form_class': BackerRegistrationForm},
        name='registration_register'),
    url(r'^accounts/login/$',
        auth_views.login,
        {'authentication_form': BackerAuthenticationForm},
        name='auth_login',
    ),
#    url(r'^register/$', 'cross_founding_platform.cross_founding.views.backer_registration'),
#    url(r'^social/', include('socialregistration.urls', namespace = 'socialregistration')),
    url(r'^accounts/', include(regUrls)),
    url(r'^accounts/profile', 'cross_founding_platform.cross_founding.views.profile'),
    url(r'^admin/', include(admin.site.urls)),
)