from django.db import models
from django.contrib.auth import get_user_model
import datetime
from dateutil import parser

# Create your models here.


class Practice(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.2/ref/models/fields/
  goal_in_minutes = models.IntegerField(default=0)
  streak_start = models.DateField(blank=True)
  last_practiced = models.DateField(blank=True)
  # one skill has many practices (from different users)
  skill = models.ForeignKey(
      'Skill',
      on_delete=models.CASCADE,
      related_name='practices'
  )

  @property
  def streak_in_days(self):
    # if we've never practiced there isnt a streak
    if self.last_practiced == None or self.streak_start == None:
      return 0

    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)


    # if we haven't practiced today or yesterday, there isn't a streak
    if self.last_practiced != today and self.last_practiced != yesterday:
      return 0

    date_delta = self.last_practiced - self.streak_start
    # add 1 for the day the streak started
    return 1 + date_delta.days

  @property
  def days_since_streak(self):
    # if we've never practiced there isnt a streak
    if self.last_practiced == None or self.streak_start == None:
      return -1

    today = datetime.date.today()
    date_delta = today - self.last_practiced
    return date_delta.days

  # Timestamps and ownership
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    return f"Practice for skill #{self.skill}"
