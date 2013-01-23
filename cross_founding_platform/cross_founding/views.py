from django.shortcuts import render_to_response
from django.template import RequestContext
from this import c


def profile(request):
    return render_to_response("profile.html")

def facebook(request):
    return render_to_response('registration/registration_form.html', c, context_instance=RequestContext(request))