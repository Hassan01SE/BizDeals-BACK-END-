from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext as _

# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, user_name, first_name, last_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, last_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email = email, user_name = user_name, first_name = first_name, last_name = last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser,PermissionsMixin):
    user_name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name', 'last_name']

    objects = CustomAccountManager()

    def __str__(self):
        return self.user_name
