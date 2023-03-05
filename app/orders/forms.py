from app.orders.models import Order
from django import forms


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'country', 'city', 'address', 'postal_code']