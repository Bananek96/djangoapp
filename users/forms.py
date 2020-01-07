from django import forms

class UserLoginForm(forms.Form):
    login = forms.CharField(
        label="Twój login",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    haslo = forms.CharField(
        label="Twoje hasło",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'})
    )