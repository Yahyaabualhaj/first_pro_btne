from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Listing, Realtor
from listings.chioces import (price_choices,
                              bedroom_choices,
                              state_choices)


def index(request):
    listings_list = Listing.objects.order_by('-list_date')
    paginator = Paginator(listings_list, 3)

    page = request.GET.get('page')
    listings = paginator.get_page(page)
    context = {'listings': listings}

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    # realtor = Realtor.objects.get(id=listing.realtor)

    context = {'listing': listing, }

    return render(request, 'listings/listing.html', context)


def search(request):
    #  QuerySet rules.

    #  Rules 1 : Sorting
    queryset_list = Listing.objects.order_by('-list_date')
    # print(Listing.objects.values())
    # print(Listing.objects.values_list('address', flat=True))
    # print(Listing.objects.values_list('address', flat=False))

    #  Rules 2 :filters == keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.\
                filter(description__icontains=keywords)

    #  Rules 3 :filters == City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list. \
                filter(description__iexact=city)

    #  Rules 4 :filters == state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list. \
                filter(description__exact=state)

    #  Rules 4 :filters == bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list. \
                filter(description__lte=bedrooms)

    #  Rules 4 :filters == price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list. \
                filter(description__lte=price)

    return render(request, 'listings/search.html', {'state_choices': state_choices,
                                                    'bedroom_choices': bedroom_choices,
                                                    'price_choices': price_choices,
                                                    'listings': queryset_list,
                                                    'values': request.GET})

