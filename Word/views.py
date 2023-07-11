from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .form import userform

def home(request):
    return render(request,"index.html")

def contactus(reuest):
    ouruser = userform()
    di = {
        'form':ouruser
    }

    return render(reuest,'sec-contact.html',di)

# class ContactVeiw(TemplateView):
#     template_name = "contact.html"

class MyView(View):
    def get(self, request):
        # Logic for GET request
        data = {'name': 'John Doe'}
        return render(request, 'contact.html', data)