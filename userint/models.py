from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Participant(models.Model):
    participant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True)
    teamname = models.CharField(max_length = 200, null = True)
    teamlead = models.CharField(max_length = 200, null = True)
    leadphone = models.CharField(max_length = 200, null = True, unique = True)
    leademail = models.CharField(max_length = 200, null = True, unique = True)
    member2 = models.CharField(max_length = 200, null = True)
    member3 = models.CharField(max_length = 200, null = True)
    member4 = models.CharField(max_length = 200, null = True)
    repolink = models.CharField(max_length = 500, null = True, unique = True)
    livelink = models.CharField(max_length = 500, null = True, unique = True)
    created_date = models.DateTimeField(default = timezone.now, null = True)

    def __str__(self):
        return self.teamname
