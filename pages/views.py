from django.shortcuts import render

from listings.models import Listing

# Create your views here.


def index(request):
    # this [:3] means only the first 3 entries will be loaded
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
