from django.contrib import admin

from .models import Delegate

# Register your models here.

admin.sites.site.register(Delegate)