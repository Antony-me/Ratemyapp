from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'rating_app'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('',views.index,name='index'),
    path('new_post', views.new_post, name='new_post'),
    url(r'^project/(\d+)$', views.project, name='project'),
    # url(r'^ajax/new_ajaxpost/$', views.new_ajaxpost, name='new_ajaxpost')
    url(r'^api/profiles/$', views.ProfileList.as_view()),
   
    
]
    
