from django.contrib import admin

# Register your models here.
from .models import Card,Settings
admin.site.register(Card)
admin.site.register(Settings)