from django import forms

from .models import chat

class chatForm(forms.ModelForm):
    class Meta:
        model = chat
        fields = ('message',)
