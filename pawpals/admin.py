from django.contrib import admin
from.models import Review
from.models import Dog
from.models import Cat
from.models import Bunnie

# Registered models so that admin has access to them
admin.site.register(Review)
admin.site.register(Dog)
admin.site.register(Cat)
admin.site.register(Bunnie)
