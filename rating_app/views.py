from rating_app.models import Post, Rating
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from .forms import NewPostForm, UpdateUserForm, UpdateUserProfileForm
# Create your views here.
def index(request):
    """
    home view function
    """
    posts = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    current_user = request.user

    return render (request, 'all_projects/index.html', {'posts':posts, 'users':users, 'user':current_user})

def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('landing')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})

def edit_profile(request):

    profile = Profile.objects.get(user=request.user)
    form = UpdateUserProfileForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False


    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True
    return render(request, 'all_projects/update.html', {'confirm':confirm, 'form':form })