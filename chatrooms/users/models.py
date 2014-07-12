from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .utils import get_gravatar_url
from .managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    gravatar_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def save(self, *args, **kwargs):
        if not self.pk:
            self.gravatar_url = get_gravatar_url(self.email)

        return super(User, self).save(*args, **kwargs)
