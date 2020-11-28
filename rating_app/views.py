from .models import Post, Rating, Profile
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import NewPostForm,  ProfileModelForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg


@login_required(login_url='/accounts/login/')
def index(request):
    """
    home view function
    """
    posts = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    current_user = request.user

    return render(request, 'all_projects/index.html', {'posts': posts, 'users': users, 'user': current_user})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('rating_app:index')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None,
                            request.FILES or None, instance=profile)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True
    return render(request, 'all_projects/update.html', {'confirm': confirm, 'form': form, 'profile': profile})


def project(request, c_id):
    current_user = request.user
    post = Post.objects.get(id=c_id)
    ratings = Rating.objects.filter(post_id=c_id)
    content = Rating.objects.filter(post_id=c_id).aggregate(Avg('content_vote'))
    design = Rating.objects.filter(post_id=c_id).aggregate(Avg('design_vote'))
    ux = Rating.objects.filter(post_id=c_id).aggregate(Avg('ux_vote'))

    ux_vote=ux["ux_vote__avg"]
    design_vote=design["design_vote__avg"]
    content_vote= content["content_vote__avg"]
    
    return render(request, 'all_projects/project.html', {"user": current_user, 'post': post, 'ratings': ratings, "design": design_vote, "content": content_vote, "ux": ux_vote})
