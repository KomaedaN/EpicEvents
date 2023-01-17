from django.db import models
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
    TEAMS = [
        ('SUPPORT', 'support'),
        ('SALES', 'sales'),
        ('ADMIN', 'admin')
    ]

    team = models.CharField(max_length=7, choices=TEAMS)


class User(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(to=Team, on_delete=models.CASCADE, null=True)
