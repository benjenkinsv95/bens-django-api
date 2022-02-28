from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Skill(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.2/ref/models/fields/
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=200, blank=True)
  review_url = models.CharField(max_length=200, blank=True)
  practice_url = models.CharField(max_length=200, blank=True)
  public = models.BooleanField(default=False)

  # Timestamps and ownership
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    return str(self.__dict__)
