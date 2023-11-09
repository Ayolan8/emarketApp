from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
        class Meta:
                model = User
                fields = ('username', 'email', 'password1', 'password2',)
    
        username = forms.CharField(label="",  widget=forms.TextInput(attrs={'placeholder' : 'Username', 'class' : 'form-control', 'style': 'maxwidth: 100%'}))
        email = forms.CharField(label="",  widget=forms.EmailInput(attrs={'placeholder' : 'Email', 'class' : 'form-control' }))
        password1 = forms.CharField(label="",  widget=forms.PasswordInput(attrs={'placeholder' : 'Enter Password', 'class' : 'form-control'}))
        password2 = forms.CharField(label="",  widget=forms.PasswordInput(attrs={'placeholder' : 'Repeat Password', 'class' : 'form-control'}))

class LoginForm(AuthenticationForm):
            class Meta:
                model = User 
                fields = ('username', 'password',)
            
            username = forms.CharField( label="",  widget=forms.TextInput(attrs={'placeholder' : 'Username', 'class' : 'form-control'}))
            password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder' : 'Enter Password', 'class' : 'form-control'}))