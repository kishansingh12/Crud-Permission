
from django.db import models
from django.utils import timezone


class Blogs(models.Model):
    class Meta:
        db_table = 'blogs'
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    excerpt = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, default='draft')
    author = models.CharField(max_length=500)

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self,mobile,email,username, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not mobile:
            raise ValueError('The given mobile must be valid')
        if not email:
            raise ValueError('The given email must be valid')    
        user = self.model(mobile=mobile,email=email,username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile, email,username, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
     
        return self._create_user(mobile, email,username, password, **extra_fields)

    def create_superuser(self, mobile,email,username, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(mobile,email,username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    mobile = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=120)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=80, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['username', 'email']
    def __str__(self):
        return self.mobile    