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

    url(r'^accounts/third_party_register/$',
        'registration.views.register',
        {'backend': 'cross_founding_platform.cross_founding.backends.ThirdPartyRegisterBackend', 'form_class': BackerRegistrationForm},
        name='third_party_register'),



    url(r'^accounts/login/$',
        'cross_founding_platform.cross_founding.views.login',
        {'authentication_form': BackerAuthenticationForm},
        name='auth_login',
    ),

    url(r'^accounts/logout/$',
        'cross_founding_platform.cross_founding.views.logout',
        {'template_name': 'registration/logout.html'},
        name='auth_logout'),

    url(r'^facebook_register/', 'cross_founding_platform.cross_founding.views.facebook_register', name='facebook_register'),

    url(r'^twitter_register/', 'cross_founding_platform.cross_founding.views.twitter_register', name='twitter_register'),

    url(r'^accounts/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'cross_founding_platform.cross_founding.views.password_reset_confirm',
        name='auth_password_reset_confirm'),

    url(r'^accounts/password/reset/$',
        'cross_founding_platform.cross_founding.views.password_reset',
        name='auth_password_reset_confirm'),

    url(r'^accounts/', include(regUrls)),
    url(r'^accounts/profile', 'cross_founding_platform.cross_founding.views.profile', name='profile'),
    url(r'^admin/', include(admin.site.urls)),
)