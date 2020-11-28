from django.urls import path
from . import views


app_name = 'rating_app'

urlpatterns = [
    path('',views.index,name='index'),
    # path('vote/', vote, name='vote'),
]