from django.contrib import admin
from .models import Receipe
# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('receipes_name', 'decription','image')
 
admin.site.register(Receipe , RecipeAdmin)