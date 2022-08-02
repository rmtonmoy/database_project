from django.shortcuts import render
from . import models
from django.http import HttpResponse
from Restaurant import models as Restaurant_models
 
# Create your views here.

def getFoodItemAction(request):
    result = models.getFoodItem(Restaurant_models.Restaurant.objects.all()[0])
    return HttpResponse(result)