from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'w-full py-4 px-6 rounded-xl border'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': 'w-full py-4 px-6 rounded-xl border'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'w-full py-4 px-6 rounded-xl border'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Re Password', 'class': 'w-full py-4 px-6 rounded-xl border'}))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'w-full py-4 px-6 rounded-xl border'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'w-full py-4 px-6 rounded-xl border'}))
