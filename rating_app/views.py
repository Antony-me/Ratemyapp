from .models import Post, Rating, Profile
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import NewPostForm,  ProfileModelForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import MerchSerializer, MerchSerializer2
from django.http import HttpResponse, Http404


class ProfileList(APIView):
    def get(self, request, format=None):
        all_merch = Profile.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST )



class ProjectList(APIView):
    def get(self, request, format=None):
        all_merch = Post.objects.all()
        serializers = MerchSerializer2(all_merch, many=True)
        return Response(serializers.data)



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


# def new_ajaxpost(request):

#     title = request.POST.get('title')
#     live_link = request.POST.get('live_link')
#     description =  request.POST.get('description')
#     developer = request.POST.get('developer')
#     image=  request.POST.get('image')

#     new_ajaxpst= Post(title=title, description=description, developer= developer, live_link=live_link, image=image)
#     new_ajaxpst.save()
    
#     data = {'success': 'You have  successfully added your peroject'}
#     return JsonResponse(data)