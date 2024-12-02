from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Receipe(models.Model):

    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True , blank=True) # models.SET_NULL if user is delelte then set null user
    receipes_name = models.CharField(max_length=30)
    decription = models.TextField()
    image = models.ImageField(upload_to="img")