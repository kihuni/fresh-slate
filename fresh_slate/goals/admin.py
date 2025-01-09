from django.contrib import admin
from .models import Goal, Milestone, DailyProgress, ProductivityPattern

# Register your models here.
admin.site.register(Goal)
admin.site.register(Milestone)
admin.site.register(DailyProgress)
admin.site.register(ProductivityPattern)
