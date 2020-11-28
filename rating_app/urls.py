from django.urls import path
from . import views


app_name = 'rating_app'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('',views.index,name='index'),
    path('new_post', views.new_post, name='new_post'),
    
]