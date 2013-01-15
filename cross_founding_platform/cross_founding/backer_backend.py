#from django.conf import settings
#from django.contrib.sites.models import RequestSite
#from django.contrib.sites.models import Site
#from django.contrib.auth.models import User
#
#from registration import signals
#from registration.models import RegistrationProfile
#
#from cross_founding_platform.cross_founding.backer_form import BackerRegistrationForm
#from cross_founding_platform.cross_founding.models import *
#
#
#class BackerBackend(object):
#
#    def register(self, request, **kwargs):
#        username, email, password = kwargs['username'],kwargs['email'], kwargs['password1']
#        if Site._meta.installed:
#            site = Site.objects.get_current()
#        else:
#            site = RequestSite(request)
#        new_user = RegistrationProfile.objects.create_inactive_user(username, email,
#            password, site)
#        signals.user_registered.send(sender=self.__class__,
#            user=new_user,
#            request=request)
#        user = User.objects.get(username=username)
#        user.first_name=kwargs['first_name']
#        user.last_name=kwargs['last_name']
##        address_user = Address()
##        address_user.save()
##        contact_user = Contact(address=address_user,email=user.email)
##        contact_user.save()
##
##        address_company = Address()
##        address_company.save()
##        contact_company = Contact(address=address_company)
##        contact_company.save()
##        company = Company(contact=contact_company, admin=user)
##        company.save()
##        user_profile = UserProfile(user=user,contact=contact_user,position='',company=company  )
##        user_profile.save()
#        user.save()
#
#        return new_user