from rest_framework import serializers
from .models import Goal, Milestone, DailyProgress, ProductivityPattern

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'

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
