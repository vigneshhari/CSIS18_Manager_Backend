from django.contrib import admin

from .models import Attendence , Track , Track_Model
# Register your models here.

admin.sites.site.register(Attendence)
admin.sites.site.register(Track)
admin.sites.site.register(Track_Model)

