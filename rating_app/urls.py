from django.urls import path
from . import views


app_name = 'rating_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('new/profile/', views.edit_profile, name='new-profile'),
    path('new_post', views.new_post, name='new_post'),
]