from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import AbstractModel
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# ORM object relational mapping


class UserManager(BaseUserManager):

    def _create_user(self, password, **kwargs):
        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, password, **kwargs):
        kwargs["is_admin"] = False
        return self._create_user(password, **kwargs)

    def create_superuser(self, password, **kwargs):
        kwargs["is_admin"] = True
        return self._create_user(password, **kwargs)


# Create your models here.


class User(AbstractModel, AbstractBaseUser):
    email = models.EmailField(
        _("Email"),
        max_length=128,
        unique=True,
        db_index=True,
    )

    bio = models.TextField(_("Bio"), blank=True)

    name = models.CharField(_("Name"), max_length=32, blank=True)

    password = models.CharField(_("Password"), max_length=128)

    is_active = models.BooleanField(
        _("Active"),
        help_text=("Designates whether this user can access their account."),
        default=True,
    )

    is_admin = models.BooleanField(
        _("Admin"),
        help_text=("Designates whether the user can log into this admin site"),
        default=False,
    )

    USERNAME_FIELD = "email"

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def __str__(self):
        return f"{self.email} ({self.name})"

    def has_perm(self, perm, obj=None):
        return self.is_admin and self.is_active

    def has_module_perms(self, app_label):
        return self.is_active and self.is_admin

    def get_all_permission(self, obj=None):
        return []

    class Meta(AbstractModel.Meta):
        verbose_name = _("User")
        verbose_name_plural = _("Users")
