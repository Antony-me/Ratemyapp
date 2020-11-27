from rating_app.models import Project, Rating
from django.shortcuts import render

# Create your views here.
def index(request):
    """
    home view function
    """
    projects = Project.objects.all()
    ratings = Rating.objects.all()

    return render (request, 'all_projects/index.html', {'projects':projects, 'ratings':ratings})