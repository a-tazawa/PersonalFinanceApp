# finance_tracker/forms.py

from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'category', 'description', 'type', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
