from django.contrib.auth.models import AbstractUser
from django.db import models

class Maker(AbstractUser):
    credit = models.DecimalField(max_digits=6, decimal_places=2, default=0)
