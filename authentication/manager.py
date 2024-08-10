# from django.contrib.auth.base_user import BaseUserManager


# class UserManager(BaseUserManager):

#     def create_user(self, contact, password=None, **extra_fields):
#         if not contact:
#             raise ValueError("enter valid contact")
        
#         user = self.model(contact = contact, **extra_fields)
#         user.set_password(password)
#         user.save(using=self.db)
#         return user    


#     def create_superuser(self, contact, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
#         extra_fields.setdefault('is_active',True)

#         return self.create_user(contact,password,**extra_fields)