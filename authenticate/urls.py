from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterAPI, HomeAPI


urlpatterns=[
    path('signup/', views.register_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name="home"),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('loginn/',TokenObtainPairView.as_view(), name='loginn'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('homeapi/', HomeAPI.as_view(), name='homeapi')
]
