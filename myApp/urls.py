from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from .views import IndexView, UserTemplateView, AutenticacaoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('auth/', AutenticacaoView.as_view(), name='auth'),
    path('login/', LoginView.as_view(template_name='user.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='logout'),
    path('user/', UserTemplateView.as_view(), name='user'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]