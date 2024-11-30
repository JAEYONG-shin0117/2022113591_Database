from django.http import JsonResponse
from django.shortcuts import render
from .models import Food, City, Country, FoodType, Allergy
from .forms import SearchFoodForm
from django.db.models import Q


def home(request):
    # 데이터베이스에서 country, city, food_type, allergy를 가져옵니다.
    countries = Country.objects.all()
    cities = City.objects.all()  # 모든 도시를 가져올 수도 있고, 특정 country에 따라 동적으로 필터링 할 수 있습니다.
    food_types = FoodType.objects.all()
    allergies = Allergy.objects.all()

    # 템플릿에 데이터를 전달
    return render(request, 'home.html', {
        'countries': countries,
        'cities': cities,
        'food_types': food_types,
        'allergies': allergies,
    })
def get_cities(request, country_id):
    # Get the cities that belong to the given country_id
    cities = City.objects.filter(country_id=country_id)

    # Prepare the data to send in the response
    cities_data = [{'id': city.id, 'city_name': city.city_name} for city in cities]

    # Return the cities data as JSON
    return JsonResponse({'cities': cities_data})

def search_view(request):
    form = SearchFoodForm(request.GET)
    foods = Food.objects.all()

    if form.is_valid():
        country = form.cleaned_data.get('country')
        city = form.cleaned_data.get('city')
        food_type = form.cleaned_data.get('food_type')
        allergy = form.cleaned_data.get('allergy')

        query = Q()  # 빈 Q 객체로 시작

        if country:
            query &= Q(country=country)
        if city:
            query &= Q(city=city)  # city 필터링 추가
        if food_type:
            query &= Q(food_type=food_type)
        if allergy:
            query &= Q(allergies__in=allergy)

        foods = foods.filter(query)

    return render(request, 'search.html', {'form': form, 'foods': foods})
