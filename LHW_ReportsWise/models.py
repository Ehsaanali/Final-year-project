from django.db import models

# Create your models here.


class LHW_ReportsWise(models.Model):
    
    District = models.CharField(max_length=255)
    Due_Reports = models.IntegerField()
    Submitted_Reports = models.IntegerField()
    def __str__(self):
        return self.Due_Reports