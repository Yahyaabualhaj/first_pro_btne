from django.shortcuts import render
from listings.models import Listing
from  realtors.models import Realtor


def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    return render(request, 'pages/index.html', {'listings': listings})


def about(request):

    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    return render(request, 'pages/about.html', {'realtors': realtors,
                                                'mvp_realtors': mvp_realtors})
