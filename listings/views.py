from django.shortcuts import render

# import to use the database info
from .models import Listing

# import to use pagination
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


def index(request):
    # this fetches the info from the database
    listings = Listing.objects.order_by('-list_date')

    # this defines how pagination will work, in this
    # case take the 'listings' and paginate 3 per page
    paginator = Paginator(listings, 3)

    # this gets which page the user is requesting
    page = request.GET.get('page')

    # this tries to fetch the page requested
    paged_listings = paginator.get_page(page)

    # this populates the info fetched from the database into
    # a dictionary
    context = {
        'listings': paged_listings
    }

    # here we pass the dictionary so that it can be used
    # in the HTML file
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
