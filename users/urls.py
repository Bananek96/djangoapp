from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
	path('', views.index, name='index'),
    path('rejestruj/', views.rejestruj, name='rejestruj'),
    path('loguj/', views.loguj_user, name='loguj'),
    path('wyloguj/', views.wyloguj_user, name='wyloguj'),
]