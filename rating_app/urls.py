from django.urls import path
from . import views
from .views import vote

app_name = 'rating_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('vote/', vote, name='vote'),
]