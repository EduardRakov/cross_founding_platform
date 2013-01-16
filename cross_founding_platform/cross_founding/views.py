from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
#from cross_founding_platform.cross_founding.backer_form import BackerForm
from cross_founding_platform.cross_founding.models import Backer

def profile(request):
    backer = User.objects.all()
    print backer
    return render_to_response("profile.html", {"backer": backer})