import datetime

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.signals import user_logged_out


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_logged_out = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


def update_logged_out(sender, user, request, **kwargs):
    user.last_logged_out = datetime.datetime.now()

user_logged_out.connect(update_logged_out)
