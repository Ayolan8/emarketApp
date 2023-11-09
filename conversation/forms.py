from django import forms
from .models import ConversationMesssage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMesssage
        fields = ['message',]

    widgets = {
        'message': forms.Textarea(attrs={
            'placeholder': 'Type your message',
            'class': 'form-control'
        }),
    }