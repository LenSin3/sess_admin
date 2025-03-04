# Create a new file called context_processors.py in your app directory

def user_profile(request):
    """Context processor to add profile picture to all templates"""
    context = {}
    
    if request.user.is_authenticated:
        try:
            # Check if the employee relationship exists first
            if hasattr(request.user, 'employee'):
                employee = request.user.employee
                context['employee'] = employee
        except Exception as e:
            # Log the specific exception (this won't show in the response)
            print(f"Error in user_profile context processor: {str(e)}")
            
    return context