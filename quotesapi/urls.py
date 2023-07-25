from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),   
    path('about.html', views.about, name="about"), 
    path('wife.html', views.wife, name="wife"), 
    path('work.html', views.work, name="work"),
    path('food.html', views.food, name="food"),
    path('random.html', views.random, name="random"),
]