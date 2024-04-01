from django.shortcuts import render
from django.conf import settings
from .models import *

def feature_enabled(id, developer):
    try:
        feature = Feature.objects.get(id=id)
    except:
        return False
    return (settings.ENVIRONMENT == 'development' and settings.DEVELOPER==developer) \
        or (feature.staging_enabled and settings.STAGING=='True') \
        or (feature.production_enabled)
