# sess_admin_portal/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfilePictureViewSet  # Import your viewset

# Create a router and register the ProfilePictureViewSet
router = DefaultRouter()
router.register(r'profile-pictures', ProfilePictureViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]