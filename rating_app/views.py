from rating_app.models import Post, Rating
from django.shortcuts import render, redirect
from .models import Profile

# Create your views here.
def index(request):
    """
    home view function
    """
    posts = Post.objects.all()
    # rating_value = Rating.objects.get(id=id)
    # print(rating_value)

    return render (request, 'all_projects/index.html', {'posts':posts})


def vote(request, post_id):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
        rating_value = Rating.objects.get(id=post_id)
        print(rating_value)

    return redirect('index')
