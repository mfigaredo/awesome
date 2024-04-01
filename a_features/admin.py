from django.contrib import admin
from .models import *

class AdminFeature(admin.ModelAdmin):
    list_display = ('name', 'id', 'developer', 'staging_enabled', 'production_enabled', )

admin.site.register(Feature, AdminFeature)


