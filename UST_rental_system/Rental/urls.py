from django.urls import path
from . import views

app_name = 'rental'
urlpatterns = [
    path('search_site/', views.search_site, name='search_site'),
    path('display_reserve_site/', views.display_reserve_site, name='display_reserve_site'),
    path('reserve_site/', views.reserve_site, name='reserve_site'),
    path('back_to_search_site/', views.back_to_search_site, name='back_to_search_site'),
    path('search_equipment/', views.search_equipment, name='search_equipment'),

]