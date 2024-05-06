from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    
    class Meta:
        model = Card
        fields = ['first_last_name', 'company_name', 'phone_number', 'email', 'vcard_address', 'photo']
        widgets = {
            'first_last_name': forms.TextInput(attrs={'placeholder': 'Twoje imię i nazwisko'}),
            'company_name': forms.TextInput(attrs={'placeholder': 'Nazwa firmy'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Numer telefonu'}),
            'email': forms.TextInput(attrs={'placeholder': 'Adres email'}),
            'vcard_address': forms.TextInput(attrs={'placeholder': 'Adres vcard'}),
        }
        labels = {
            'first_last_name': '',
            'company_name': '',
            'phone_number': '',
            'email': '',
            'photo': 'Zdjęcie (najlepiej kwadrat)',
            'vcard_address': '',
        }