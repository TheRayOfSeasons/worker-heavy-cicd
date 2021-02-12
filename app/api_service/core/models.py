import datetime

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class TimeStampedModel(models.Model):
    """
    A model that tracks audit times.
    """

    datetime_created = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )
    datetime_modified = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class UserTrailModel(models.Model):
    """
    Records the user who edited the value.
    """

    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_created_set",
    )
    modified_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_modified_set",
    )

    class Meta:
        abstract = True


class SoftDeletableModel(models.Model):
    """
    Adds a soft delete functionality to a model.
    """

    is_active = models.BooleanField(default=True)
    deleted_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_deleted_set",
    )
    datetime_deleted = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        abstract = True

    def soft_delete(self, user=None):
        """
        Soft deletes the model instance's data in the database.

            :param user: :type User:
                - The user responsible for deletion. Can be optional.
        """
        self.is_active = False
        self.datetime_deleted = datetime.datetime.now()
        fields = ['is_active', 'datetime_deleted']
        if user:
            self.user = user
            fields.append('deleted_by')
        self.save(update_fields=fields)


class BaseModel(TimeStampedModel, UserTrailModel, SoftDeletableModel):
    """
    A base model that combines the functionalities
    of all other abstract models.
    """

    class Meta:
        abstract = True
