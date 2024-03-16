from django import forms
from payment.models import ShippingAddress


class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'shipping_full_name': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Full Name', 'required': True}),
            'shipping_email': forms.EmailInput(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Email', 'required': True}),
            'shipping_address1': forms.Textarea(attrs={'class': 'form-control','rows': 1, 'placeholder': 'Address1', 'required': True}),
            'shipping_address2': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Address2', 'required': False}),
            'shipping_city': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'City', 'required': True}),
            'shipping_state': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'State', 'required': False}),
            'shipping_zipcode': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Zipcode', 'required': False}),
            'shipping_country': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Country', 'required': True}),
        }
