from rest_framework import serializers
from .models import UserSubmission

class UserSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubmission
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'comment', 'attached_file', 'agreement']
