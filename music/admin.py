from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Actor,Movie,Casting, Commit
admin.site.register([Actor,Movie,Casting,Commit])
