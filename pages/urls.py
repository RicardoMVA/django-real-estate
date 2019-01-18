# this is needed to define a path using 'path()', which will
# fetch from the 'views.py' the urls we'll use
from django.urls import path

# read this as 'from all, import viwes'
from . import views

urlpatterns = [
    # this is fetching the root/index page defined in the 
    # 'views.py' file
    path('', views.index, name='index')
]
