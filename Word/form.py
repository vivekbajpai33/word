from django import forms
from customuser. models import user

 

class userform(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':"form-control"}))
    email = forms.CharField(max_length=100)
    dp = forms.FileField(max_length=500)
    password = forms.CharField(max_length=100)
