from pickletools import read_long1
from api.serializers import UserSerializer
from rest_framework import serializers
from django.db.models import fields

from .models.skill import Skill
from .models.practice import Practice

class SkillSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Skill
        fields = '__all__'

class PracticeSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(read_only=True)

    class Meta:
        model = Practice
        fields = ('id', 'goal_in_minutes', 'streak_start',
                  'last_practiced', 'streak_in_days', 'days_since_streak', 'skill')
