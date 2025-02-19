from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Permission
from django.db.models import Q
from django.core.validators import EmailValidator,RegexValidator
from admin_settings.views.delivery_status import DeliveryStatus

class Role(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    permissions = models.ManyToManyField(Permission, blank=True)
    delivery_status = models.ManyToManyField(DeliveryStatus, blank=True)

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
    phone_regex = RegexValidator( regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    email = models.EmailField(verbose_name="email", max_length=255, unique=True,validators=[EmailValidator(message="Enter a valid email address.")])
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True,validators=[phone_regex])
    role =models.ForeignKey(Role, on_delete=models.CASCADE,blank=True,null=True)
    full_name = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True)
    address = models.TextField(blank=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_phone_verified = models.BooleanField(default=False)
    phone_verified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    soft_delete=models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """
        Check if the user has a specific permission.
        This method is called by Django's permission framework.

        :param perm: The permission string, e.g., 'app_label.permission_codename'
        :param obj: The object for which the permission is checked (optional)
        :return: True if the user has the permission, False otherwise
        """
        # Superusers have all permissions
        if self.is_superuser:
            return True

        # Check if any of the user's roles have the specified permission
        if self.role:
            # Use Q objects to build OR conditions for permissions
            # This checks if any of the user's roles have the permission
            if self.role.permissions.filter(Q(codename=perm) | Q(content_type__app_label=perm.split('.')[0])).exists():
                return True

        return False
    def has_specific_perm(self, codename):
        """
        Check if the user has a specific permission (by codename).
        This method is called to check for a specific permission.

        :param codename: The codename of the permission, e.g., 'change_specific_role'
        :return: True if the user has the permission, False otherwise
        """
        # Superusers have all permissions
        if self.is_superuser:
            return True

        # Check if any of the user's roles have the specified permission
        if self.role:
            # Check if the role has the specific permission by codename
            if self.role.permissions.filter(codename=codename).exists():
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