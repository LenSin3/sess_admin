# your_app/serializers.py
"""
Serializers for the API

from rest_framework import serializers
from .models import ProfilePicture

class ProfilePictureSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProfilePicture
        fields = ['id', 'image', 'uploaded_at', 'content_object', 'image_url']

    def get_image_url(self, obj):
        return obj.image_url()
    
from django.contrib.admin.models import LogEntry

class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = ['id', 'action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag', 'change_message']

"""

        
        
###############################################################################
from rest_framework import serializers
from .models import ProfilePicture
from django.contrib.admin.models import LogEntry

class ContentObjectSerializer(serializers.Serializer):
    # No Meta class needed here!
    def to_representation(self, instance):
        if isinstance(instance, LogEntry):
            return {"error": "LogEntry instances are not allowed"}
        
        return {
            "id": instance.id,
            "name": getattr(instance, 'name', None) 
                    or getattr(instance, 'username', None)
                    or f"{getattr(instance, 'first_name', '')} {getattr(instance, 'last_name', '')}".strip()
                    or str(instance)
        }

class ProfilePictureSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    content_object = ContentObjectSerializer(read_only=True)  # Add this line

    class Meta:
        model = ProfilePicture
        fields = ['id', 'image', 'uploaded_at', 'content_object', 'image_url']

    def get_image_url(self, obj):
        return obj.image_url()

class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = ['id', 'action_time', 'user', 'content_type', 'object_id', 
                 'object_repr', 'action_flag', 'change_message']