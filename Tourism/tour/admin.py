from django.contrib import admin

# Register your models here.
from .models import Contact,Rate


admin.site.register(Contact)
admin.site.register(Rate)