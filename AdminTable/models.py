from django.db import models
from RestaurantManager import models as RestaurantManager_models
from Restaurant import models as Restaurant_models

# Create your models here.
class AdminTable(models.Model):
    class Meta:
            unique_together = (('m_id', 'r_id'),)
            
    m_id = models.ForeignKey(RestaurantManager_models.RestaurantManager, on_delete = models.CASCADE)
    r_id = models.ForeignKey(Restaurant_models.Restaurant, on_delete = models.CASCADE)
    
    

def get_Admin(restaurant):
    return AdminTable.objects.filter(r_id = restaurant)