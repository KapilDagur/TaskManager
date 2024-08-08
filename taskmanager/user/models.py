import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, username, phone, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        if not phone:
            raise ValueError('The Phone field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, phone, password, **extra_fields)
    
    def delete_user(self, user_id):
        try:
            user = self.get(user_id=user_id)
            user.delete()
            return True
        except self.model.DoesNotExist:
            return False

    def update_user(self, user_id, **kwargs):
        try:
            user = self.get(user_id=user_id)
            for key, value in kwargs.items():
                setattr(user, key, value)
            user.save(using=self._db)
            return user
        except self.model.DoesNotExist:
            return None

class User(AbstractBaseUser, PermissionsMixin):
    
    #Enum for Gender
    class GenderChoices(models.TextChoices):
        MALE    = ('M', 'Male')
        FEMALE  = ('F', 'Female')
        OTHER   = ('O', 'Other')
        
    #ENUM for Role
    class RoleChoices(models.TextChoices):
        MANAGER     = ('MANAGER', 'Manager')
        TEAM_LEAD   = ('TEAM_LEAD', 'Team Lead')
        EMPLOYEE    = ('EMPLOYEE', 'Employee')

    user_id     = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email       = models.EmailField(unique=True)
    username    = models.CharField(max_length=30, unique=True)
    phone       = models.CharField(max_length=15, unique=True)
    first_name  = models.CharField(max_length=30, blank=True)
    last_name   = models.CharField(max_length=30, blank=True)
    gender      = models.CharField(max_length=1, choices=GenderChoices.choices, blank=True)
    role        = models.CharField(max_length=10, choices=RoleChoices.choices, default=RoleChoices.EMPLOYEE)
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):
        return self.username
