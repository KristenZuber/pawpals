from django.contrib import admin
from.models import Profile, Apply

# Register models so the admin has access to them easily
admin.site.register(Profile)
admin.site.register(Apply)
