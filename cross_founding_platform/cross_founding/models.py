from django.db import models
from django.contrib.auth.models import User, UserManager

class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Backer(models.Model):
    test_field = models.CharField(max_length=10)

    def __unicode__(self):
        return self.test_field

class CustomUser(User):
    location = models.CharField(max_length=20)
    project_owner = models.ForeignKey(Project, null=True)
    backer = models.ForeignKey(Backer, null=True)
    objects = UserManager()