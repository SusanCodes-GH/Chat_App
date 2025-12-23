from django.contrib import admin
from .models import Profile, Friend, Chatmsg

# Register your models here.
admin.site.register([Profile, Friend, Chatmsg])