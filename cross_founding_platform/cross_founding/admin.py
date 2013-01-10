from django.contrib import admin
from cross_founding_platform.cross_founding.models import User, Project, Backer, CustomUser

admin.site.register(CustomUser)
admin.site.register(Project)
admin.site.register(Backer)