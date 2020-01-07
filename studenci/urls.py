from django.urls import path
from . import views

from django.views.generic import ListView
from studenci.models import Miasto

app_name = 'studenci'
urlpatterns = [
	path('', views.index, name='index'),
	path('miasta/', ListView.as_view(
		model=Miasto,
		context_object_name='miasta',
		template_name='studenci/lista_miast.html'
	), name='miasta_lista'),
	path('miasta/dodaj', views.miasta, name='miasta_dodaj'),
	path('uczelnie/dodaj', views.uczelnie, name='uczelnie_dodaj'),
	path('uczelnie/lista', views.ListaUczelni.as_view(), name='uczelnie_lista'),
	path('login/', views.loguj_studenta, name='login'),
]