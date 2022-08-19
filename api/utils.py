from typing import List
import statistics

from .models import Restaurant

def get_restaurants_rating_average(restaurant_list: List[Restaurant]) -> float:
    return statistics.mean([restaurant.rating for restaurant in restaurant_list])

def get_restaurants_rating_standard_deviation(restaurant_list: List[Restaurant]) -> float:
    return statistics.stdev([restaurant.rating for restaurant in restaurant_list])
