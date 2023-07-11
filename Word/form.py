from django import forms


class userform(forms.Form):
    car = forms.CharField(max_length=100)
    price = forms.CharField(max_length=100)