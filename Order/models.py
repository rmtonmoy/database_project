from django.db import models
from DeliveryAddress import models as DeliveryAddress_models
from Customer import models as Customer_models
from Restaurant import models as Restaurant_models
# Create your models here.

class Order(models.Model):
    date = models.DateField()
    a_id = models.ForeignKey(DeliveryAddress_models.DeliveryAddress, on_delete = models.CASCADE)
    c_id = models.ForeignKey(Customer_models.Customer, on_delete = models.CASCADE)
    r_id = models.ForeignKey(Restaurant_models.Restaurant, on_delete = models.CASCADE)
    