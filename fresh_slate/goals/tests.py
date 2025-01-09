from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Goal, Milestone, DailyProgress, ProductivityPattern

User = get_user_model()

class GoalModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.goal = Goal.objects.create(
            user=self.user,
            title='Test Goal',
            description='Test Description',
            priority='MEDIUM',
            status='ACTIVE'
        )

    def test_goal_creation(self):
        self.assertEqual(self.goal.title, 'Test Goal')
        self.assertEqual(self.goal.description, 'Test Description')
        self.assertEqual(self.goal.priority, 'MEDIUM')
        self.assertEqual(self.goal.status, 'ACTIVE')

class MilestoneModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.goal = Goal.objects.create(
            user=self.user,
            title='Test Goal',
            description='Test Description',
            priority='MEDIUM',
            status='ACTIVE'
        )
        self.milestone = Milestone.objects.create(
            goal=self.goal,
            title='Test Milestone',
            completed=False,
            due_date='2023-12-31'
        )

    def test_milestone_creation(self):
        self.assertEqual(self.milestone.title, 'Test Milestone')
        self.assertFalse(self.milestone.completed)
        self.assertEqual(str(self.milestone.due_date), '2023-12-31')

class DailyProgressModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.daily_progress = DailyProgress.objects.create(
            user=self.user,
            date='2023-12-31',
            morning_reflection='Morning reflection',
            evening_reflection='Evening reflection',
            mood_score=5,
            productivity_score=7
        )

    def test_daily_progress_creation(self):
        self.assertEqual(str(self.daily_progress.date), '2023-12-31')
        self.assertEqual(self.daily_progress.morning_reflection, 'Morning reflection')
        self.assertEqual(self.daily_progress.evening_reflection, 'Evening reflection')
        self.assertEqual(self.daily_progress.mood_score, 5)
        self.assertEqual(self.daily_progress.productivity_score, 7)

class ProductivityPatternModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.productivity_pattern = ProductivityPattern.objects.create(
            user=self.user,
            day_of_week=0,
            peak_start_time='09:00:00',
            peak_end_time='11:00:00',
            effectiveness_score=8.5
        )

    def test_productivity_pattern_creation(self):
        self.assertEqual(self.productivity_pattern.day_of_week, 0)
        self.assertEqual(str(self.productivity_pattern.peak_start_time), '09:00:00')
        self.assertEqual(str(self.productivity_pattern.peak_end_time), '11:00:00')
        self.assertEqual(self.productivity_pattern.effectiveness_score, 8.5)
