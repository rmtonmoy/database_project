from django.db import models
from Restaurant import models as Restaurant_models
# Create your models here.


class FoodItem(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField(default = 0)
    r_id = models.ForeignKey(Restaurant_models.Restaurant, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name