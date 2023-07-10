# from django.contrib.auth.base_user import BaseUserManage

# class UserManeger(BaseUserManage):
#     def creat_user(self,phone_number,password = None,**extra_field):
#         if not phone_number:
#             raise ValueError("phone number is requird")
        
#         extra_field ['email'] = self.normalize_field(extra_field['email'])
#         user = self.model(phone_number = phone_number,**extra_field)
#         user.set_password(password)
#         user.save(using = self.db)

#         return user
#     def create_superuser(self,phone_number,password = None,**extra_field):
#         extra_field.setdefault('is_staff',True)
#         extra_field.setdefault('is_superuser',True)
#         extra_field.setdefault('is_active',True)

#         return self.creat_user(phone_number,password,**extra_field)