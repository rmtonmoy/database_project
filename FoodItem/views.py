from django.shortcuts import render
from . import models
from django.http import HttpResponse
from Restaurant import models as Restaurant_models
 
# Create your views here.
nm = ''
def getFoodItemAction(request):
    global nm
    
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="restaurantName":
                nm = value
        result = models.getFoodItem(Restaurant_models.Restaurant.objects.get(name = nm))
        context = {'result': result}
        return render(request, 'general_result.html', context)
    
    return render(request,'general_form.html')