from django.db import models
from django.contrib.auth.models import User, UserManager


class Backer(User):
    dob_at = models.DateField()
    location = models.CharField(max_length=100)

    objects = UserManager()