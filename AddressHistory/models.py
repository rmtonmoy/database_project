from django.db import models
from Customer import models as Customer_models
from DeliveryAddress import models as DeliveryAddress_models
# Create your models here.

class AddressHistory(models.Model):
    class Meta:
        unique_together = (('c_id', 'a_id'),)
    c_id = models.ForeignKey(Customer_models.Customer, on_delete = models.CASCADE)
    a_id = models.ForeignKey(DeliveryAddress_models.DeliveryAddress, on_delete = models.CASCADE)
    