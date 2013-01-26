from django.contrib import admin
from django.conf.urls import patterns, include, url

import registration.backends.default.urls as regUrls

from cross_founding_platform.cross_founding.forms import BackerRegistrationForm

from cross_founding_platform.cross_founding.backer_registration import *

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^accounts/register/$',
        'registration.views.register',
        {'backend': 'registration.backends.default.DefaultBackend', 'form_class': BackerRegistrationForm},
        name='registration_register'),

#    url(r'^register/$', 'cross_founding_platform.cross_founding.views.backer_registration'),
    url(r'^social/', include('socialregistration.urls', namespace = 'socialregistration')),
    url(r'^accounts/', include(regUrls)),
    url(r'^accounts/profile', 'cross_founding_platform.cross_founding.views.profile'),
    url(r'^admin/', include(admin.site.urls)),
)