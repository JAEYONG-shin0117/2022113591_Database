# Generated by Django 5.1.3 on 2024-11-29 02:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_type_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='food_recommendation.country')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('restaurant_name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_recommendation.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_recommendation.country')),
            ],
        ),
        migrations.CreateModel(
            name='FoodAllergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_recommendation.allergy')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_recommendation.food')),
            ],
            options={
                'unique_together': {('food', 'allergy')},
            },
        ),
        migrations.AddField(
            model_name='food',
            name='allergies',
            field=models.ManyToManyField(through='food_recommendation.FoodAllergy', to='food_recommendation.allergy'),
        ),
        migrations.AddField(
            model_name='food',
            name='food_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_recommendation.foodtype'),
        ),
    ]
