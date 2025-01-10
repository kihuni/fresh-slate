from rest_framework import serializers
from .models import Goal, Milestone, DailyProgress, ProductivityPattern

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'title', 'description', 'priority', 'status', 'created_at', 'target_date', 'completed', 'parent_goal']

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'

class DailyProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyProgress
        fields = '__all__'

class ProductivityPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductivityPattern
        fields = '__all__'
