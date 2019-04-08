from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Listing
from listings.chioces import (price_choices)


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
    queryset_list = []
    # print(Listing.objects.values_list('state'))
    # print(Listing.objects.values_list('address', flat=True))

    #  QuerySet rules.

    #  Rules 1 : Sorting
    # listings = Listing.objects.order_by('-list_date')

    state_choices = remove_dup_get(Listing, 'state')
    city_choices = remove_dup_get(Listing, 'city')
    print('city_choices : %s' % city_choices)
    bedrooms_choices = remove_dup_get(Listing, 'bedrooms')

    rules = Q(bedrooms__gte=0)

    #  Rules 2 :filters == keywords
    if 'keywords' in request.GET:
        keywords_val = request.GET['keywords']
        if keywords_val:
            rules &= Q(description__icontains=keywords_val)

    #  Rules 3 :filters == City
    if 'city' in request.GET:
        city_val = request.GET['city']
        if city_val:
            rules = rules & Q(city__iexact=city_val)

    #  Rules 4 :filters == state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            rules = rules & Q(state__iexact=state)

    #  Rules 4 :filters == bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            rules = rules & Q(bedrooms__gte=bedrooms)

    #  Rules 4 :filters == price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            rules = rules & Q(price__lte=price)

    if rules:
        queryset_list = Listing.objects.filter(rules)

    context = {'state_choices': state_choices,
               'city_choices': city_choices,
               'bedrooms_choices': bedrooms_choices,
               'price_choices': price_choices,
               'listings': queryset_list,
               'values': request.GET}

    return render(request, 'listings/search.html', context)


def remove_dup_get(model, f_name):
    dict = []
    for item in model.objects.values_list(f_name, flat=True):
        if item not in dict:
            dict.append(item)
    return dict
