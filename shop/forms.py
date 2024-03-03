from django import forms
from shop.models import Shop


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your lesson title'}),
            'price': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your product price'}),
            'description1': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Please enter your description'}),
            'description2': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Please enter your description'}),
            'description3': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Please enter your description'}),
            'description4': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Please enter your description'}),
            'description5': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Please enter your description'}),
            'description6': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Please enter your description'}),
            'description7': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Please enter your description'}),
            'description8': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Please enter your description'}),
            'description9': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Please enter your description'}),
            'description10': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Please enter your description'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, initial=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
