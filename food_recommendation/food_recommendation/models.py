from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    currency = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    population = models.IntegerField()

    class Meta:
        db_table = 'country'  # 실제 테이블 이름

    def __str__(self):
        return self.country_name

class City(models.Model):
    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'city'  # 실제 테이블 이름

    def __str__(self):
        return self.city_name

class Allergy(models.Model):
    allergy_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'allergy'  # 실제 테이블 이름

    def __str__(self):
        return self.allergy_name

class FoodType(models.Model):
    food_type_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'food_type'  # 실제 테이블 이름

    def __str__(self):
        return self.food_type_name

class Food(models.Model):
    food_name = models.CharField(max_length=100)
    description = models.TextField()
    restaurant_name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    allergies = models.ManyToManyField(Allergy, through='FoodAllergy')

    class Meta:
        db_table = 'food'  # 실제 테이블 이름

    def __str__(self):
        return self.food_name

class FoodAllergy(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)

    class Meta:
        db_table = 'food_allergy'  # 실제 테이블 이름
        unique_together = ('food', 'allergy')

    def __str__(self):
        return f'{self.food} - {self.allergy}'
