from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext

from cross_founding_platform.cross_founding.forms import BackerRegistrationForm
from cross_founding_platform.cross_founding.models import Backer

def profile(request):
    return render_to_response("profile.html")

@csrf_protect
def backer_registration(request, *args, **kwargs):

    if request.method == "POST":
        form = BackerRegistrationForm(request.POST)

        if form.is_valid():
            user = User()
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password1']
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.save()

            backer = Backer(user=user)
            backer.gender = form.cleaned_data["gender"]
            backer.location = request.META['REMOTE_ADDR']
            backer.dob_at = form.cleaned_data['dob_date']
            backer.save()
            return HttpResponseRedirect('/accounts/register/complete/')
    else:
        form = BackerRegistrationForm()

    context = {'form': form}

    return render_to_response('registration/registration_form.html', context,
        context_instance=RequestContext(request))