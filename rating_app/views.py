from rating_app.models import Post, Rating
from django.shortcuts import render, redirect
from .models import Profile

# Create your views here.
def index(request):
    """
    home view function
    """
    projects = Post.objects.all()
    ratings = Rating.objects.all()

    return render (request, 'all_projects/index.html', {'projects':projects, 'ratings':ratings})


# def rate_project(request, project):
#     current_user = request.user
#     rating_value = Rating.objects.get(id=project.id)
#     if rating_value.rating.filter(id=current_user.id).exists():
#         rating_value.rating.remove(current_user)
#     else:
#         rating_value.rating.add(current_user)
#     return redirect('index')
