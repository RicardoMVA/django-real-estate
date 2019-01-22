from django.contrib import admin
# importing the class inside the 'models.py' file
from .models import Listing

# Register your models here.

admin.site.register(Listing)
