from django.contrib import admin
from .models import Profile,Projects,Review

from django.contrib import admin

# Register your models here.

admin.site.register(Profile)
admin.site.register(Projects)
admin.site.register(Review)