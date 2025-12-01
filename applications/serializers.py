from rest_framework import serializers

from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")
    cv = serializers.FileField(required=True) 
    class Meta:
        model = Application
        fields = [
            "id", "user", "job", "cv", "cover_letter", "status", "created_at"
        ]
        read_only_fields = ["status", "created_at"]
