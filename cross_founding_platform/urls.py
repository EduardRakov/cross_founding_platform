from django.contrib import admin
from django.conf.urls import patterns, include, url
from registration.views import register
from cross_founding_platform.cross_founding.backer_form import BackerRegistrationForm

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cross_founding_platform.views.home', name='home'),
    # url(r'^cross_founding_platform/', include('cross_founding_platform.foo.urls')),
#    (r'^accounts/', include('registration.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),

#    url(r'^accounts/register/$',  register, { 'backend': 'cross_founding.backer_backend.BackerBackend' }, name='registration_register'),
    (r'^accounts/register/$', 'registration.views.register', {'form_class':BackerRegistrationForm}),
    url(r'^accounts/profile', 'cross_founding_platform.cross_founding.views.profile'),
#    url(r'^cfp/sign_up_form', 'cross_founding_platform.cross_founding.views.sign_up_form'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)