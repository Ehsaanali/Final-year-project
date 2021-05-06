

from django.db import models

# Create your models here.
class Division(models.Model):
    div_name = models.CharField(max_length=50)
    Total_Cases = models.IntegerField()
    Treatement_Completed = models.IntegerField()
    Treatement_Incompleted = models.IntegerField()
    No_of_Death = models.IntegerField()

    class Meta:
        verbose_name_plural = "Division"
        


    def __str__(self):
        return self.div_name




