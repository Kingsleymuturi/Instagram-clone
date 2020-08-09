from django.urls import path, include
from instagram.views import PostLikeToggle, PostLikeAPIToggle
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('profile/<username>/', views.profile, name='profile'),
    
    
    
    
    
    
    
    
]