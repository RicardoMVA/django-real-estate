from django.shortcuts import render, get_object_or_404

# import to use the database info
from .models import Listing

# import to use pagination
from django.core.paginator import Paginator

# used in the search
from listings.choices import bedroom_choices, price_choices, state_choices


# Create your views here.


def index(request):
    # this fetches the info from the database
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # this defines how pagination will work, in this
    # case take the 'listings' and paginate 3 per page
    paginator = Paginator(listings, 3)

    # this gets which page in pagination the user is requesting
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
    # this takes to 404 page if the listing doesn't exists
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # check if 'keywords' form received input by user
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            # this filters the results so that only the ones
            # that contains inside its 'description' field what
            # was passed in the 'keywords' form will be shown
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
    else:
        keywords = ''

    # check if 'city' form received input by user
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            # this filters the results so that only the ones
            # that contains exactly the 'city' that was passed
            # in the 'city' form will be shown (case insensitive)
            queryset_list = queryset_list.filter(
                city__iexact=city)
    else:
        city = ''

    # check if 'state' form received input by user
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            # this filters the results so that only the ones
            # that contains exactly the 'state' that was passed
            # in the 'state' form will be shown (case insensitive)
            queryset_list = queryset_list.filter(
                state__iexact=state)
    else:
        state = ''

    # check if 'bedrooms' form received input by user
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            # this filters the results so that only the ones
            # that contains up to the number of 'bedrooms' that
            # was passed in the 'bedrooms' form will be shown
            # ('lte' stands for 'less than or equal to')
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)
    else:
        bedrooms = ''

    # check if 'price' form received input by user
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            # this filters the results so that only the ones
            # that contains up to the number of 'price' that was
            # passed in the 'price' form will be shown
            queryset_list = queryset_list.filter(
                price__lte=price)
    else:
        price = ''

    # this defines how pagination will work, in this
    # case take the 'listings' and paginate 3 per page
    paginator = Paginator(queryset_list, 3)

    # this gets which page in pagination the user is requesting
    page = request.GET.get('page')

    # this tries to fetch the page requested
    paged_listings = paginator.get_page(page)

    # this passes the search options to the search page
    # passing 'keywords' is important for the pagination, to
    # keep the query strings between pages
    context = {
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'listings': paged_listings,
        'values': request.GET,
        'keywords': keywords,
        'city': city,
        'state': state,
        'bedrooms': bedrooms,
        'price': price,
    }
    return render(request, 'listings/search.html', context)
