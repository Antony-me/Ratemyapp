from collections import namedtuple
from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'rating_app'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('',views.index,name='index'),
    path('ajax/new_post/', views.new_post, name='new_post'),
    url(r'^project/(\d+)$', views.project, name='project'),
    url(r'^api/profiles/$', views.ProfileList.as_view(), name='profiles_api'),
    url(r'^api/projects/$', views.ProjectList.as_view(), name='projects_api'),  
]
    
