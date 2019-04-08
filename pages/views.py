from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.chioces import (price_choices,
                              bedroom_choices,
                              state_choices)


def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    # listing = Listing.objects.values()
    state_choices = remove_dup_get(Listing, 'state')
    city_choices = remove_dup_get(Listing, 'city')
    bedrooms_choices = remove_dup_get(Listing, 'bedrooms')

    return render(request, 'pages/index.html', {'listings': listings,
                                                'state_choices': state_choices,
                                                'city_choices': city_choices,
                                                'bedrooms_choices': bedrooms_choices,
                                                'price_choices': price_choices
                                                })


def about(request):

    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    return render(request, 'pages/about.html', {'realtors': realtors,
                                                'mvp_realtors': mvp_realtors})


# def remove_dup_get(model_obj, f_name):
#     dict = []
#     for item in model_obj:
#         if item[f_name] not in dict:
#             dict.append(item[f_name])
#     return dict

def remove_dup_get(model, f_name):
    dict = []
    for item in model.objects.values_list(f_name, flat=True):
        if item not in dict:
            dict.append(item)
    return dict