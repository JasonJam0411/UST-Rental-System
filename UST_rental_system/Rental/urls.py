from django.urls import path
from . import views

app_name = 'rental'
urlpatterns = [
    path('member_search_site/', views.member_search_site, name='member_search_site'),
    #path('login/', views.login, name='login')
]