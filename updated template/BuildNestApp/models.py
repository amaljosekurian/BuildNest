from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)

class Usertable(AbstractUser):
    username = models.CharField(max_length=150, unique=True)  # Add username field
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    is_contractor = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_purchase_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
# class Worker(models.Model):
#     worker_id = models.CharField(max_length=10)
#     worker_name = models.CharField(max_length=100)
#     worker_region = models.CharField(max_length=100)
#     worker_job_role = models.CharField(max_length=100)
#     salary = models.DecimalField(max_digits=10, decimal_places=2)
#     # site = models.ForeignKey(Site, on_delete=models.CASCADE)
#     # contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    

