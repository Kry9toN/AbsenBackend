from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class AccountManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Username harus di isi')
        user = self.model(
            username = username
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, password=None):
        if not username:
            raise ValueError('Username harus di isi')
        user = self.model(
            username = username
        )
        user.is_dudi = True
        user.is_guru = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self.db)
        return user

class Account(AbstractBaseUser):

    username = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    is_dudi = models.BooleanField(default=False)
    is_guru = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    longitude = models.IntegerField(default=0)
    latitude = models.IntegerField(default=0)

    objects = AccountManager()
    
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Absen(models.Model):
    name = models.CharField(max_length=200)
    longitude = models.IntegerField(default=0)
    latitude = models.IntegerField(default=0)

    def __str__(self):
        self.name