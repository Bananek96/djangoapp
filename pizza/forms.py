from django.forms import ModelForm, ModelMultipleChoiceField, Textarea

from pizza.models import Pizza, Skladnik

class PizzaForm(ModelForm):
    skladniki = ModelMultipleChoiceField(queryset=Skladnik.objects.all())
    class Meta:
        model = Pizza
        exclude = ('data',)
        widgets = {
            'opis': Textarea(attrs={'cols': 40, 'rows': 2}),
        }

class SkladnikForm(ModelForm):
    class Meta:
        model = Skladnik
        fields = ('nazwa', 'jarski', 'pizze')