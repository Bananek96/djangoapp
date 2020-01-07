from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse

from studenci.models import Miasto, Uczelnia
from studenci.forms import UserLoginForm, UczelniaForm, MiastoForm

from django.views.generic import ListView

def index(request):
    # return HttpResponse("<h1>Witaj wsród sudentów!</h1>")
    return render(request,'studenci/index.html')


def miasta(request):
    """Widok wyświetlający miasta i formularz ich dodawania"""
    if request.method == 'POST':
        # nazwa = request.POST.get('nazwa', '')
        # kod = request.POST.get('kod', '')
        form = MiastoForm(request.POST)
        # if len(nazwa.strip()) and len(kod.strip()):
        if form.is_valid():
            #m = Miasto(nazwa=nazwa, kod=kod)
            m = Miasto(nazwa=form.cleaned_data['nazwa'], kod=form.cleaned_data['kod'])
            m.save()
            messages.success(request, "Poprawnie dodano dane!")
            return redirect(reverse('studenci:miasta'))
        else:
            messages.error(request, "Niepoprawne dane!")
    else:
        form = MiastoForm()

    miasta = Miasto.objects.all()
    kontekst = {'miasta': miasta, 'form': form}
    return render(request, 'studenci/miasta.html', kontekst)


# nazwa = request.POST.get('nazwa', '')
# if len(nazwa.strip()):

def uczelnie(request):
    """Widok wyświetlający miasta i formularz ich dodawania"""
    if request.method == 'POST':
        form = UczelniaForm(request.POST)  # do wyjaśnienie
        if form.is_valid():
            print(form.cleaned_data)
            u = Uczelnia(nazwa=form.cleaned_data['nazwa'])
            u.save()
            messages.success(request, "Poprawnie dodano dane!")
            return redirect(reverse('studenci:uczelnie'))
        else:
            messages.error(request, "Niepoprawne dane!")
    else:
        form = UczelniaForm()

    uczelnie = Uczelnia.objects.all()
    kontekst = {'uczelnie': uczelnie, 'form': form}

    if request.user.has_perm('studenci.add_uczelnia'):
        return render(request, 'studenci/uczelnie.html', kontekst)
    else:
        messages.info(request, "Nie możesz dodawać uczelni!")
        return redirect(reverse('studenci:index'))

class ListaUczelni(ListView):
    model = Uczelnia
    context_object_name = 'uczelnie'
    template_name = 'studenci/lista_uczelni.html'

def loguj_studenta(request):
    if request.method == 'POST':
        pass
    else:
        form = UserLoginForm()
    kontekst = {'form': form}
    return render(request, 'studenci/login.html', kontekst)