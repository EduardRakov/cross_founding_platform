from django.db import models
from django.contrib.auth.models import User, UserManager


class Backer(User):
    gender = models.CharField(max_length=6)
    dob_at = models.DateField()
    location = models.CharField(max_length=50)

    objects = UserManager()