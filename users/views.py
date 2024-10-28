from rest_framework import viewsets
from .models import UserSubmission
from .serializers import UserSubmissionSerializer

# Create your views here.
class UserSubmissionViewSet(viewsets.ModelViewSet):
    queryset = UserSubmission.objects.all()
    serializer_class = UserSubmissionSerializer


