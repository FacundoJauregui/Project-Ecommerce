from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(required = True, widget = forms.TextInput(attrs = {'class':"uk-input",'placeholder':"Enter First Name"}))
    last_name = forms.CharField(required = True, widget = forms.TextInput(attrs = {'class':"uk-input",'placeholder':"Enter Last Name"}))
    username = forms.CharField(required = True, widget = forms.TextInput(attrs = {'class':"uk-input",'placeholder':"Enter Username"}))
    email = forms.EmailField(required = True, widget = forms.TextInput(attrs = {'class':"uk-input",'placeholder':"Enter Email"}))
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(attrs = {'class':"uk-input",'placeholder':"Enter Password"}))
    password2 = forms.CharField(label= 'Confirmar contraseña', widget = forms.PasswordInput(attrs = {'class':"uk-input",'placeholder':"Confirm Password"}))
    
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2',
                ]
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs = {'class':"uk-input",'placeholder':"Enter Username"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs ={'class':"uk-input",'placeholder':"Enter Password"}))