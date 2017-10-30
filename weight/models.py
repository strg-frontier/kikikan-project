from django.db import models

# Create your models here.
class Weight(models.Model):
  user_id = models.IntegerField()
  date = models.DateTimeField()
  weight = models.IntegerField()
