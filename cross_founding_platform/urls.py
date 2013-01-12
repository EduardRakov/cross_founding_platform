from django.contrib import admin
from django.conf.urls import patterns, include, url

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cross_founding_platform.views.home', name='home'),
    # url(r'^cross_founding_platform/', include('cross_founding_platform.foo.urls')),
    url(r'^cfp/sign_up_form', 'cross_founding_platform.cross_founding.views.sign_up_form'),
    url(r'^cfp/profile', 'cross_founding_platform.cross_founding.views.profile'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)