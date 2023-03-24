from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import List, Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['list']

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = '__all__'
        exclude = ['host']

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email","password1", "password2"]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user