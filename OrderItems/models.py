from django.db import models
from Order import models as Order_models
from FoodItem import models as FoodItem_models

# Create your models here.

class OrderItems(models.Model):
    class Meta:
        unique_together = (('o_id', 'f_id'),)
        
    f_quantity = models.IntegerField(default = 0)
    o_id = models.ForeignKey(Order_models.Order, on_delete = models.CASCADE)
    f_id = models.ForeignKey(FoodItem_models.FoodItem, on_delete = models.CASCADE)
    