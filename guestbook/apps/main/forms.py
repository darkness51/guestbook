from django import forms
from main.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message