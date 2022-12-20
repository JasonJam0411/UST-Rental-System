from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home-nu/',views.index, name='home-nu')

]