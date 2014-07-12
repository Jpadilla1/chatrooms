from django.db import models
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager
from .utils import get_gravatar_url


class User(AbstractBaseUser):
    class Meta:
        ordering = ['username', ]

    username = models.CharField(
        'username', max_length=30, unique=True,
        help_text='Required. 30 characters or fewer. Letters, digits and '
                  '@/./+/-/_ only.',
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                'Enter a valid username. '
                'This value may contain only letters, numbers '
                'and @/./+/-/_ characters.', 'invalid'),
        ],
        error_messages={
            'unique': "A user with that username already exists.",
        })

    gravatar_url = models.URLField(blank=True)
    email = models.EmailField('email address', blank=True, unique=True)
    is_staff = models.BooleanField(
        'staff status', default=False,
        help_text='Designates whether the user can log into this admin '
                  'site.')
    is_active = models.BooleanField(
        'active', default=True,
        help_text='Designates whether this user should be treated as '
                  'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.pk or self.has_field_changed('email'):
            self.gravatar_url = get_gravatar_url(self.email)

        return super(User, self).save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
