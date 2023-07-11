from django.contrib import admin
from  customuser.models import user

class usersAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','dp')

admin.site.register(user,usersAdmin)    

# Register your models here.
