from django import forms

class LocationForm(forms.Form):
    store_number = forms.CharField(label='Store Number', max_length=15)
    store_name = forms.CharField(label='Store Name', max_length=15)
    ownership = forms.CharField(label='Ownership', max_length=15)
    address = forms.CharField(label='Street Address', max_length=40)
    city = forms.CharField(label='City', max_length=15)
    postcode = forms.CharField(label='Postcode', max_length=15)
    country = forms.CharField(label='Country', max_length=15)
    phone = forms.CharField(label='Phone Number', max_length=40)