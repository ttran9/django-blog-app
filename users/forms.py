from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # the model that we want this form to interact with.
        # when this form validates it creates a user.
        model = User
        # fields to be shown on the form in a specified order.
        fields = ['username' ,'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        # the model that we want this form to interact with.
        # when this form validates it creates a user.
        model = User
        # fields to be shown on the form in a specified order.
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
