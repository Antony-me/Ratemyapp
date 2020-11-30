from .models import Post, Rating, Profile
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import NewPostForm,  ProfileModelForm, RatingForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import MerchSerializer, MerchSerializer2
from django.http import HttpResponse, Http404
from .utilis import truncate


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


    def post(self, request, format=None):
        serializers = MerchSerializer2(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST )




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
    form = NewPostForm()
    # if request.method == 'POST':
    #     form = NewPostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('project')
    if request.is_ajax():
        form = NewPostForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    
    return render(request, 'all_projects/new_post.html', {"form": form})


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

    
    ux_vote=truncate(ux["ux_vote__avg"], 2)
    design_vote=truncate(design["design_vote__avg"], 2)
    content_vote= truncate(content["content_vote__avg"], 2)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project = post
            rating.user = current_user.profile
            rating.save()
            return render(request, 'all_projects/project.html', {"user": current_user, 'form':form, 'post': post, 'ratings': ratings, "design": design_vote, "content": content_vote, "ux": ux_vote})
    else:
        form = RatingForm()

    return render(request, 'all_projects/project.html', {"user": current_user, 'form':form, 'post': post, 'ratings': ratings, "design": design_vote, "content": content_vote, "ux": ux_vote})


