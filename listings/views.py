from django.shortcuts import render

# import to use the database info
from .models import Listing

# Create your views here.


def index(request):
    # this fetches the info from the database
    listings = Listing.objects.all()

    # this populates the info fetched from the database into
    # a dictionary
    context = {
        'listings': listings
    }

    # here we pass the dictionary so that it can be used
    # in the HTML file
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
