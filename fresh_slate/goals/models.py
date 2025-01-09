from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Goal(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]
    
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('EVOLVED', 'Evolved'),
        ('ARCHIVED', 'Archived'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='MEDIUM')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    target_date = models.DateField(null=True, blank=True)
    parent_goal = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Milestone(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name='milestones')
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    due_date = models.DateField()
    completed_at = models.DateTimeField(null=True, blank=True)

class DailyProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    morning_reflection = models.TextField(blank=True)
    evening_reflection = models.TextField(blank=True)
    mood_score = models.IntegerField(null=True, blank=True)
    productivity_score = models.IntegerField(null=True, blank=True)
    
    class Meta:
        unique_together = ['user', 'date']

class ProductivityPattern(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day_of_week = models.IntegerField()  # 0-6 for Monday-Sunday
    peak_start_time = models.TimeField()
    peak_end_time = models.TimeField()
    effectiveness_score = models.FloatField()
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'day_of_week']