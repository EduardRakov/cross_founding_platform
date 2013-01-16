from django.db import models
from django.contrib.auth.models import User, UserManager

class Backer(User):
    gender = models.CharField(max_length=2)
    dob_at = models.DateField()
    profession = models.CharField(blank=True, max_length=15)
    location = models.CharField(max_length=16)

    objects = UserManager()