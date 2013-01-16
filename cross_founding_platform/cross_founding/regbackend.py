#from django.contrib.auth.models import User
#from django.contrib.sites.models import Site, RequestSite
#from registration import signals
#from registration.models import RegistrationProfile
#
#def register(self, request, **kwargs):
#    """
#    Given a username, email address and password, register a new
#    user account, which will initially be inactive.
#
#    Along with the new ``User`` object, a new
#    ``registration.models.RegistrationProfile`` will be created,
#    tied to that ``User``, containing the activation key which
#    will be used for this account.
#
#    An email will be sent to the supplied email address; this
#    email should contain an activation link. The email will be
#    rendered using two templates. See the documentation for
#    ``RegistrationProfile.send_activation_email()`` for
#    information about these templates and the contexts provided to
#    them.
#
#    After the ``User`` and ``RegistrationProfile`` are created and
#    the activation email is sent, the signal
#    ``registration.signals.user_registered`` will be sent, with
#    the new ``User`` as the keyword argument ``user`` and the
#    class of this backend as the sender.
#
#    """
#    username, email, password = kwargs['username'], kwargs['email'], kwargs['password1']
#    if Site._meta.installed:
#        site = Site.objects.get_current()
#    else:
#        site = RequestSite(request)
#    new_user = RegistrationProfile.objects.create_inactive_user(username, email,
#        password, site)
#    signals.user_registered.send(sender=self.__class__,
#        user=new_user,
#        request=request)
#    u = User.objects.get(username=new_user.username)
#    u.first_name = kwargs['first_name']
#    u.last_name = kwargs['last_name']
#    u.save()
#
#    return new_user
