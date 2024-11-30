from django import forms
from .models import Country, City, Allergy, FoodType


class SearchFoodForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=False)
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False)  # 자동 필터링 제거
    food_type = forms.ModelChoiceField(queryset=FoodType.objects.all(), required=False)
    allergy = forms.ModelMultipleChoiceField(queryset=Allergy.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    # __init__에서 country_id 관련 코드를 제거
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # city 필드는 country_id와 무관하게 기본적으로 모든 도시 목록을 보여줌
