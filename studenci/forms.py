from django import forms

class UserLoginForm(forms.Form):
    login = forms.CharField(
        label="Twój login",
        max_length=20,
        widget=forms.TextInput()
    )


class UczelniaForm(forms.Form):
    nazwa = forms.CharField(
        label="Nazwa uczelni",
        max_length=30,
        widget=forms.TextInput()
    )

class MiastoForm(forms.Form):
    nazwa = forms.CharField(
        label="Nazwa miasta",
        max_length=30,
        widget=forms.TextInput()
    )
    kod = forms.CharField(
        label="Kod pocztowy",
        max_length=6,
        widget=forms.TextInput()
    )

# github.com/lo1cgsan/djangoapp1