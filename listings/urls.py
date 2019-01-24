# this is needed to define a path using 'path()', which will
# fetch from the 'views.py' the HTML we'll use
from django.urls import path

# read this as 'from all, import viwes'
from . import views

# fetch your routes here
urlpatterns = [
    # this is fetching the root/index page defined in the
    # 'views.py' file, where we define that all '/listings'
    # should load what's stored here, that's why we don't
    # need to specify '/listings/something'
    path('', views.index, name='listings'),
    # this will fetch the listing id
    path('<int:listing_id>', views.listing, name='listing'),
    # used to submit search form
    path('search', views.search, name='search'),
]
