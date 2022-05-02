from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
class StudentManager(BaseUserManager):
    
    def create_user(self, name, x, y, password = None, active = True, staff = False, admin = False):

        user = self.model(
            name = name
        )

        user.set_password(password)
        user.x = x
        user.y = y
        user.active = active
        user.staff = staff
        user.admin = admin
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, name, x, y, password = None):

        user = self.create_user(
            name, 
            x = x,
            y = y,
            password= password,
            active=True,
            staff = True,
            admin = False
        )

        return user

    def create_superuser(self, name,x,y, password = None):

        user = self.create_user(
            name, 
            x = x,
            y = y,
            password= password,
            active = True,
            staff = True,
            admin = True
        )

        return user

class Student(AbstractBaseUser):
    
    name = models.CharField(max_length=20, unique=True)
    x = models.IntegerField(default=1)
    y = models.IntegerField(default=1)
    active = models.BooleanField()
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    
# Turning Student to AUTH_USER in DB
    manager = StudentManager()

    USERNAME_FIELD = 'name'

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def is_staff(self):
        return self.staff

    def is_admin(self):
        return self.admin
    
