from django.db import models

# Create your models here.
class LHW_Areawise(models.Model):
    
    month = models.TextField()
    exp = models.IntegerField()
    Covered_UC = models.IntegerField()
    def __str__(self):
        return self.month
