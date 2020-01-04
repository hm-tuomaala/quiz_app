from django import forms

class LoginForm(forms.Form):
    key = forms.CharField(required=True, label='Syötä saamasi koodi:', max_length=6,
            widget=forms.TextInput(attrs={'placeholder': 'Koodi'}))
    name = forms.CharField(required=True, label='Syötä nimesi:', max_length=100,
            widget=forms.TextInput(attrs={'placeholder': 'Nimi'}))
