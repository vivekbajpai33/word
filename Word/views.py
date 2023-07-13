from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from .form import userform
from customuser.models import user

def home(request):
    return render(request,"index.html")


def contactus(reuest):
    ouruser = userform()
    
    di = {
        'form':ouruser
    }



    return render(reuest,'sec-contact.html',di)
    

class ContactVeiw(View):
    
    def soem(self,request):
        if request.method == 'get':
            data  = user.objects.all()
        return render(request,'customer.html',data)

    def get(self, request):
            return render(request,'customer.html')
    
    def post(self,request):
         if request.method == 'POST':
              
              username = request.POST.get('username')
              useremail = request.POST.get('useremail')
              userdp = request.FILES['userdp']
              userpassword = request.POST.get('userpassword')
              print('userdp', userdp)

              data = user(name=username,email= useremail,dp=userdp,password= userpassword)
              data.save()
              

              return render(request,'customer.html')


class Studentview(View):
     def get(self,request):
          home = user.objects.all()
          di = {
               'our':home
          }
          return render(request,'student.html',di)


def update(request):
     if request.method == 'POST':
          name = request.POST.get('name')
          email = request.POST.get('email')
          password = request.POST.get('password')
          dp = request.POST.get('dp')
          emp = user(id = id,name= name,email=email,password= password,dp =dp)     
          emp.save()
          return redirect("student")  
     return render(request,'student.html')      


class MyView(View):
    def get(self, request):
        home  = user.objects.all()
        data = {
             
             'use' : home
            }
        
        return render(request, 'contact.html', data)