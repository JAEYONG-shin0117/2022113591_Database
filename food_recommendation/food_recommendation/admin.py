from django.contrib import admin
from .models import Country, City, Allergy, FoodType

admin.site.register(Country)
admin.site.register(City)
admin.site.register(FoodType)
admin.site.register(Allergy)


