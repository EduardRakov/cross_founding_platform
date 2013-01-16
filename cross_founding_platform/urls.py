from django.contrib import admin
from django.conf.urls import patterns, include, url
import registration.backends.default.urls as regUrls

from cross_founding_platform.cross_founding.forms import BackerRegistrationForm


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cross_founding_platform.views.home', name='home'),
    # url(r'^cross_founding_platform/', include('cross_founding_platform.foo.urls')),
#    (r'^accounts/', include('registration.urls')),
#    (r'^accounts/', include('registration.backends.default.urls')),

#    (r'^accounts/register/$', 'registration.views.register', {'form_class':BackerRegistrationForm}),
#
    url(r'^accounts/register/$',
        'registration.views.register',
        {'backend': 'registration.backends.default.DefaultBackend', 'form_class': BackerRegistrationForm},
        name='registration_register'),

    url(r'^accounts/',  include(regUrls)),
#    url(r'^accounts/activate/complete/$', 'gamb.profile.views.redirect_after_activation'),

#    url(r'^accounts/register/$',
#        register,
#        {'backend': 'accounts.regbackend.RegBackend','form_class':BackerRegistrationForm},
#        name='registration_register'
#    ),

    url(r'^accounts/profile', 'cross_founding_platform.cross_founding.views.profile'),
#    url(r'^cfp/sign_up_form', 'cross_founding_platform.cross_founding.views.sign_up_form'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)