from django.db import models

# Create your models here.
class Message_bord(models.Model):
  new_message=models.TextField(null=False)
