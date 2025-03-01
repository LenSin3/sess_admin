from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings

class LoginRequiredMiddleware:
    """
    Middleware to redirect unauthenticated users to the login page
    for all URLs except those in the exempted list.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        # List of URLs that don't require authentication
        self.exempt_urls = [
            reverse('login'),
            '/admin/',  # Explicitly add admin URL
            '/admin/login/',  # Add admin login URL
        ]
    
    def __call__(self, request):
        # If user is not authenticated and trying to access a protected URL
        if not request.user.is_authenticated:
            current_path = request.path_info
            
            # Check if the current path is exempt
            if not any(exempt_url in current_path for exempt_url in self.exempt_urls):
                # Check for static files
                if not current_path.startswith(settings.STATIC_URL):
                    # Redirect to login page with the next parameter
                    return redirect(f"{reverse('login')}?next={current_path}")
        
        response = self.get_response(request)
        return response