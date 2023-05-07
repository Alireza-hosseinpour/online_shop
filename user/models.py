from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.modules import path_and_rename


class User(AbstractUser):
    phone_number = models.CharField(max_length=11)
    address = models.TextField()
    avatar = models.ImageField(upload_to=path_and_rename('users'), null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number} {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "users"
        verbose_name_plural = "users"
        db_table = "users"
