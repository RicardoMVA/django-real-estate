from django.shortcuts import render

from listings.models import Listing
from realtors.models import Realtor

# Create your views here.


def index(request):
    # this [:3] means only the first 3 entries will be loaded
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # get all realtors

    realtors = Realtor.objects.order_by('-hire_date')

    # get seller of the month
    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)
