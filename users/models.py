from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


from django.contrib.auth.models import Permission


class Role(models.Model):
    name = models.CharField(max_length=100)
    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'roles'
    

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    role =models.ForeignKey(Role, on_delete=models.CASCADE,blank=True,null=True)
    full_name = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active = models.BooleanField(default=True)
    soft_delete=models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Check if the user's role has the specified permission
        if self.is_admin:
            return True
        return False

    def has_module_perms(self, app_label):
        return True
    class Meta:
        db_table = 'users'

from django.utils import timezone

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        # Current time with timezone awareness
        now = timezone.now()
        # Time limit for the OTP to be valid, say 5 minutes
        valid_until = self.timestamp + timezone.timedelta(minutes=5)
        return now <= valid_until

    class Meta:
        db_table = 'OTPs'