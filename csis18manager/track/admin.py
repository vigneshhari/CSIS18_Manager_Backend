from django.contrib import admin

from .models import Attendence , Track
# Register your models here.

admin.sites.site.register(Attendence)
admin.sites.site.register(Track)
