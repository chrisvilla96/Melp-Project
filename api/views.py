from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from .models import Restaurant
from .serializers import RestaurantSerializer
from . import utils

class RestaurantList(generics.ListCreateAPIView):
    """View for Listinig Restaurants in API"""

    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for Detail Restaurant API Endpoints"""

    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

@csrf_exempt
def get_nearby_restaurants_count(request):
    """View for retrieving nerby restaurants given a radious"""

    try:
        data = {}

        latitude = float(request.GET.get('latitude', None))
        longitude = float(request.GET.get('longitude', None))
        radious = float(request.GET.get('radious', None))

        current_location = (latitude, longitude)

        valid_restaurants = []

        restaurants = Restaurant.objects.all()

        for restaurant in restaurants:

            distance_to_restaurant: float = restaurant.meters_between_location(current_location)

            if distance_to_restaurant <= radious:
                valid_restaurants.append(restaurant)


        data['count'] = len(valid_restaurants)
        data['avg'] = utils.get_restaurants_rating_average(valid_restaurants)
        data['std'] = utils.get_restaurants_rating_standard_deviation(valid_restaurants)
        data['message'] = 'Valid Request'

        return JsonResponse(data, status=200)


    except Exception:

        data["message"] = "Hubo un error en el request"
        return JsonResponse(data, status=400)


