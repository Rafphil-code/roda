from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={"placeholder" : "user@gmail.com", "class":"w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    username = forms.CharField(label="Nom et Prénoms", widget=forms.TextInput(attrs={"placeholder":"Jean Pierre", "class":"w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder":"Entrez votre mot de passe", "class":"w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"placeholder":"Resaisissez votre mot de passe", "class":"w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"}))

    class Meta:
        model = get_user_model()
        fields = ["email", "username", "password1", "password2"]