from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(profile)
admin.site.register(room)
admin.site.register(room_image)
admin.site.register(room_review)