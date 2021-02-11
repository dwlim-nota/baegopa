from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, user_id, name=None, bank_name=None, bank_account_number=None, password=None):
        if not name:
            name=user_id
        user = self.model(
            name=name,
            user_id=user_id,
            bank_name=bank_name,
            bank_account_number=bank_account_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password):
        user = self.create_user(
            user_id=user_id,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Member(AbstractBaseUser):
    user_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=30, null=True)
    bank_account_number = models.BigIntegerField(null=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'user_id'

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

