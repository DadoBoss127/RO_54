from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput
from django import forms

from shop.models import Profile


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'username',
                  'email')

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})


class UpdateUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('first_name', 'last_name',
                  'username',
                  'email')

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
        }

class ChangePasswordForm(SetPasswordForm):
    class Mete:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your NEW password'})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please confirm your NEW password'})

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'old_cart']
        widgets = {
            'phone': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Your phone number', 'required': True}),
            'address1': forms.Textarea(attrs={'class': 'form-control','rows': 1, 'placeholder': 'Address1', 'required': True}),
            'address2': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Address1', 'required': False}),
            'city': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'City', 'required': True}),
            'state': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'State', 'required': True}),
            'zipcode': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Zipcode', 'required': True}),
            'country': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Country', 'required': True}),
        }