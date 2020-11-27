from django.shortcuts import render

# Create your views here.
def index(request):
    """
    home view function
    """
    return render(request, 'all_projects/index.html')