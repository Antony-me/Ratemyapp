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
    return render(request, 'newpost.html', {"form": form})

def edit_profile(request):
    
    
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile')
            # return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)

    params = {
        # 'images' : images,   
        'user_form': user_form,
        'prof_form': prof_form,
        
    }
    return render(request, 'new_profile.html', params )