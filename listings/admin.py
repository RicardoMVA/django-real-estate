from django.contrib import admin
# importing the class inside the 'models.py' file
from .models import Listing

# Register your models here.

class ListingAdmin(admin.ModelAdmin):


admin.site.register(Listing)
