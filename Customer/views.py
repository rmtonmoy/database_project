from django.shortcuts import render
from .models import Customer
# Create your views here.

first_name = ''
last_name = ''
email = ''
pwd = ''

def signaction(request):
    global first_name,last_name, email, pwd
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="firstname":
                first_name=value
            if key=="lastname":
                last_name =value
            if key=="email":
                email =value
            if key=="password":
                pwd =value
        
    customer = Customer(name = first_name + last_name, address = email, password = pwd)
    if(len(customer.name) > 0):
        customer.save() 


    return render(request,'registration.html')
    
    
    
def homeaction(request):
    return render(request,"home.html")
    
    
    
# Create your views here.
def loginaction(request):
    global email, pwd
    
    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="email":
                email = value
            if key=="password":
                pwd = value
        
        customer = Customer.objects.get(address = email)
        
        if customer.password != pwd:
            return render(request,'error.html')
        else:
            return render(request,"home.html")

    return render(request,'Loginp.html')