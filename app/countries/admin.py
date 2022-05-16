from django.contrib import admin

from .models import Country, HostCountry

admin.site.register(Country)
admin.site.register(HostCountry)