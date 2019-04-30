from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
import pytz


class UserProfile(models.Model):

    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.username
