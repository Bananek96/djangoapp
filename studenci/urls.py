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
	path('miasta/create', views.DodajMiasto.as_view(), name='miasta_create'),
	path('uczelnie/create', views.DodajUczelnie.as_view(), name='uczelnie_create'),
	path('uczelnie/edytuj/<int:pk>', views.EdytujUczelnie.as_view(), name='uczelnie_edytuj'),
	path('uczelnie/usun/<int:pk>', views.UsunUczelnie.as_view(), name='uczelnie_usun'),
	path('miasta/edytuj/<int:pk>', views.EdytujMiasta.as_view(), name='miasta_edytuj'),
	path('miasta/usun/<int:pk>', views.UsunMiasta.as_view(), name='miasta_usun'),
	path('login/', views.loguj_studenta, name='login'),
]