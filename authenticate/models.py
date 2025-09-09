from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname,  phonenumber,password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not phonenumber:
            raise ValueError("Phone number is required")
        if not firstname:
            raise ValueError("Firstname is required")
        if not lastname:
            raise ValueError("Lastname is required")
        
        email=self.normalize_email(email)
        user=self.model(
            email=email,
            firstname=firstname,
            lastname=lastname,
            phonenumber=phonenumber,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, firstname, lastname, phonenumber, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not password:
            raise ValueError("Superuser must have password")
        return self.create_user(email, firstname, lastname, phonenumber, password, **extra_fields)

    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email=models.CharField(max_length=30, unique=True)
    phonenumber=models.CharField(max_length=20)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    date_joined=models.DateTimeField(default=timezone.now)

    objects=CustomUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['firstname', 'lastname','phonenumber']

    def __str__(self):
        return f"{self.email}"
