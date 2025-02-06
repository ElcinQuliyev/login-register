from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login,  logout 
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import (
    RegisterForm, 
    LoginForm,
    ProfileForm,

)


appname = 'accounts'


def home(request):
    """
    Home view that displays both registration and 
    login forms and handles their submissions.
    """
    register_form = register_view(request)
    login_form = login_view(request)
    profile_form = profile_view(request)

    context = {
            "register_form": register_form,
            "login_form": login_form,
            "profile_form":profile_form,
        }
    
    return render(
        request,
        "index.html",
        context
    )


def register_view(request):
    """Handles user registration. """
    register_form = RegisterForm()

    if request.method == "POST":
        register_form = RegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save(False)
            return redirect('profile')

    return register_form




def login_view(request):
    """Handles user login. """  
    login_form = LoginForm()
        
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            print(login_form.cleaned_data['email'])
            print(login_form.cleaned_data['password'])
            user = authenticate(
                request,
                email=login_form.cleaned_data['email'],
                password=login_form.cleaned_data['password'],
            )
            if not user:
                messages.add_message(request, messages.ERROR, "Successfully Sent!")
                print('not found')
            else:
                print('user found')
                django_login(request, user)
                return redirect('profile')
            
    return  login_form


# @property
# def get_photo_url(self):
#     if self.image and hasattr(self.image, 'url'):
#         return self.photo.url
#     return "/static/media/media/default_img.png"



@login_required(login_url='profile')
def profile_view(request):
    return render(request, 'profile.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def auth_settings_view(request):
    profile_form = ProfileForm()
    register_form = RegisterForm()
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        register_form = RegisterForm(request.POST, request.FILES, instance=request.user)
        if profile_form.is_valid() and register_form.is_valid():
            profile_form.save()
            register_form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')
        print('profile_update', profile_form, register_form)

    django_login(request, user=request.user)
    return render(request, 'auth_settings.html')






# from django.contrib.auth.views import LoginView as DjangoLoginView
# from django.urls import reverse_lazy

# class LoginView(DjangoLoginView):
#     template_name = "profile.html"
#     success_url = reverse_lazy("accounts:profile")
