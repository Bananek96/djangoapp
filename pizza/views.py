from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from pizza.models import Pizza, Skladnik
from pizza.forms import PizzaForm, SkladnikForm

def index(request):
    # return HttpResponse("<h1>Witaj w barze Pizza!</h1>")
    return render(request,'pizza/index.html')


def dodajPizza(request):
    if request.method == 'POST':
        pass
        # form = PizzaForm(request.POST)
        # if form.is_valid():
        #     print(form.cleaned_data)
    else:
        form = PizzaForm()
    return render(request,'pizza/pizzaform.html', {'form': form})


def dodajSkladnik(request):
    if request.method == 'POST':
        form = SkladnikForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            s = Skladnik(
                nazwa=form.cleaned_data['nazwa'],
                jarski=form.cleaned_data['jarski']
            )
            s.save()
            messages.success(request, "Dodano składnik!")
            return redirect(reverse('pizza:index'))
    else:
        form = SkladnikForm()
    return render(request,'pizza/skladnikform.html', {'form': form})