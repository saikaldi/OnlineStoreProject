from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserSubmissionViewSet

# Set up the router
router = DefaultRouter()
router.register(r'submissions', UserSubmissionViewSet, basename='user-submission')

urlpatterns = [
    path('', include(router.urls)),
]
