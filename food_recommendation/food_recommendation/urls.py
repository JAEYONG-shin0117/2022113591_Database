from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 홈 페이지
    path('search/', views.search_view, name='search'),  # 검색 결과 페이지
    path('get_cities/<int:country_id>/', views.get_cities, name='get_cities'),  # 나라에 맞는 도시 목록을 가져오는 URL
]
