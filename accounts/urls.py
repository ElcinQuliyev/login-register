from django.urls import path
from .views import (
    home,
    register_view,
    login_view,
    profile_view,
    logout_view,
    auth_settings_view,
    # LoginView
)


urlpatterns = [
    path('home/', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/settings', auth_settings_view, name='auth-settings'),
    # path(
    #     "test-login/", 
    #     LoginView.as_view(),
    #     name="test-login"
    # ),
]