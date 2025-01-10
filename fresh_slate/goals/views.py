from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Goal, Milestone, DailyProgress, ProductivityPattern
from .serializers import (
    GoalSerializer, 
    MilestoneSerializer,
    DailyProgressSerializer,
    ProductivityPatternSerializer
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class RegisterView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class GoalViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def evolve(self, request, pk=None):
        """Evolve a goal based on progress and create a new version"""
        original_goal = self.get_object()
        
        # Create new evolved goal
        new_goal = Goal.objects.create(
            user=request.user,
            title=f"Evolved: {original_goal.title}",
            description=request.data.get('new_description', original_goal.description),
            parent_goal=original_goal
        )
        
        # Mark original goal as evolved
        original_goal.status = 'EVOLVED'
        original_goal.save()
        
        return Response(GoalSerializer(new_goal).data)

    @action(detail=True, methods=['delete'])
    def delete_goal(self, request, pk=None):
        """Delete a goal and return a success message"""
        goal = self.get_object()
        goal.delete()
        return Response({"detail": "Goal was deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class DailyProgressViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DailyProgressSerializer
    queryset = DailyProgress.objects.all()

    def get_queryset(self):
        return DailyProgress.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def today(self, request):
        """Get or create today's progress entry"""
        progress, created = DailyProgress.objects.get_or_create(
            user=request.user,
            date=timezone.now().date()
        )
        return Response(DailyProgressSerializer(progress).data)

class ProductivityPatternViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductivityPatternSerializer
    queryset = ProductivityPattern.objects.all()

    def get_queryset(self):
        return ProductivityPattern.objects.filter(user=self.request.user)

    @action(detail=False, methods=['get'])
    def analyze_patterns(self, request):
        """Analyze user's productivity patterns and return insights"""
        patterns = self.get_queryset()
        
        # Calculate peak productivity times and best days
        peak_times = patterns.order_by('-effectiveness_score')
        best_day = peak_times.first()
        
        return Response({
            'best_day': best_day.day_of_week if best_day else None,
            'peak_start_time': best_day.peak_start_time if best_day else None,
            'peak_end_time': best_day.peak_end_time if best_day else None,
            'effectiveness_score': best_day.effectiveness_score if best_day else None
        })

class MilestoneViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MilestoneSerializer
    queryset = Milestone.objects.all()

    def get_queryset(self):
        return Milestone.objects.filter(goal__user=self.request.user)