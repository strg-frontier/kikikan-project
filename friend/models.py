from django.db import models

# Create your models here.
class Friend(models.Model):
    requested_user = models.IntegerField()
    follow_user = models.IntegerField()
    request_state = models.IntegerField(default=0)