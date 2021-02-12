import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    """
    This extends the base user model with
    custom fields and model methods.
    """

    display_name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'A user with this email already exists.'
        }
    )

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    is_cms_admin = models.BooleanField(
        default=False,
        help_text=(
            'Designates whether user can edit site content '
            'through the custom CMS.'
        )
    )

    USERNAME_FIELD = 'display_name'

    def __str__(self):
        return self.username
