from django.db import models

# Create your models here.
class Students_data(models.Model):
    name = models.CharField(max_length=30 , null=True)
    email = models.EmailField(max_length=15)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name