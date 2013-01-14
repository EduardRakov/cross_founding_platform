from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from cross_founding_platform.cross_founding.forms import BackerForm
from cross_founding_platform.cross_founding.models import Backer

def profile(request):
    backer = Backer.objects.all()
    return render_to_response("profile.html", {"backer": backer})


@csrf_exempt
def sign_up_form(request, student_id=None):

    if student_id is None:
        backer = Backer()
    else:
        backer = get_object_or_404(Backer, id=student_id)

    if request.POST:
        backer_form = BackerForm(request.POST, instance=backer)
        if backer_form.is_valid():
            backer_form.save()
            return HttpResponseRedirect("")
    else:
        backer_form = BackerForm(instance=backer)

    return render_to_response("registration/registration_form.html", { "backer_form": backer_form})