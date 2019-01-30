from django.contrib import admin
# importing the class inside the 'models.py' file
from .models import Listing

# Register your models here.
# this is used to personalize the info displayed in admin area


class ListingAdmin(admin.ModelAdmin):
    # select the info that you want to show up based on model
    list_display = (
        'id',
        'title',
        'is_published',
        'price',
        'list_date',
        'realtor'
    )
    # defines clickable objects
    list_display_links = ('id', 'title')
    # filter box
    list_filter = ('realtor',)
    # allow for clicking checkboxes
    list_editable = ('is_published',)
    # search fields
    search_fields = (
        'title',
        'description',
        'address',
        'city',
        'state',
        'zipcode',
        'price'
    )
    # defines pagination
    list_per_page = 25


# pass both the model and the personalized display
admin.site.register(Listing, ListingAdmin)
