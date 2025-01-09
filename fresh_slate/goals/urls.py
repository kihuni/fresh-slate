from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import LoginView
from .views import GoalViewSet, MilestoneViewSet, DailyProgressViewSet, ProductivityPatternViewSet, RegisterView

router = DefaultRouter()
router.register(r'goals', GoalViewSet)
router.register(r'milestones', MilestoneViewSet)
router.register(r'daily-progress', DailyProgressViewSet)
router.register(r'productivity-patterns', ProductivityPatternViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
]
