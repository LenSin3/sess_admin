# your_app/serializers.py
from rest_framework import serializers
from .models import ProfilePicture

class ProfilePictureSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProfilePicture
        fields = ['id', 'image', 'uploaded_at', 'content_object', 'image_url']

    def get_image_url(self, obj):
        return obj.image_url()