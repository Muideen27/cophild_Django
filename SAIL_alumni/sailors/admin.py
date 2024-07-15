from django.contrib import admin
from .models import Sailor, Profile, Connection

# Register your models here.
admin.site.register(Sailor)
admin.site.register(Profile)
admin.site.register(Connection)
