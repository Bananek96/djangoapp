from django.urls import path
from . import views

app_name = 'pizza'
urlpatterns = [
	path('', views.index, name='index'),
    path('pizza/dodaj', views.dodajPizza, name='pizza_add'),
    path('skladnik/dodaj', views.dodajSkladnik, name='skladnik_add'),
]