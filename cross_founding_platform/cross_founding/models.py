from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Backer(models.Model):
    pass

class User(models.Model):
    user_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=50)
    e_mail = models.EmailField()
    password = models.CharField(max_length=25)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    location = models.CharField(max_length=20)
    project_owner = models.ForeignKey(Project)
    backer = models.ForeignKey(Backer)


    def __unicode__(self):
        return self.user_name
