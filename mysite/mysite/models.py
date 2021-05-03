from django.db import models

class Admin(models.Model):
    admin_name = models.CharField(max_length=50)
    admin_last_name = models.CharField(max_length=50)

# one to one relationship
# each User has one Profile
# each Profile has one User
class Profile(models.Model):
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    admin = models.OneToOneField(Admin, on_delete=models.CASCADE, primary_key=True)
