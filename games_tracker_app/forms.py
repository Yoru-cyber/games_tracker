from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'rating', 'genre', 'release_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'nes-input'}),
            'rating': forms.NumberInput(attrs={'class': 'nes-input'}),
            'genre': forms.Select(attrs={'class': 'nes-select'}),
            'release_date': forms.DateInput(attrs={'class': 'nes-input', 'type': 'date'}),
        }