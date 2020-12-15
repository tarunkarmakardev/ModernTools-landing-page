from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('profile/', views.profile, name="profile"),
]
