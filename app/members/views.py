from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
try:
    p2.restaurant
except ObjectDoesNotExist:
    print("There is no restaurant here.")

    hasattr(p2, 'restaurant')