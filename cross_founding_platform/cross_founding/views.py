from django.contrib.auth.models import User
from django.shortcuts import render_to_response

def profile(request):
    backer = User.objects.all()
    print backer
    return render_to_response("profile.html", {"backer": backer})