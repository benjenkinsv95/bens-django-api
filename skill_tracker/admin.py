from django.contrib import admin
from .models.skill import Skill
from .models.practice import Practice

# Register your models here.
admin.site.register(Skill)
admin.site.register(Practice)
