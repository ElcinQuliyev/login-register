from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,  logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.contrib import messages


def home(request):
    """
    Home view that displays both registration and 
    login forms and handles their submissions.
    """
    register_form = register_view(request)
    login_form = login_view(request)


    context = {
            "register_form": register_form,
            "login_form": login_form,
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
            user = authenticate(
                request,
                username=login_form.cleaned_data.get('username'),
                password=login_form.cleaned_data.get('password'),
            )

            if user is not None:
                login(request, user)
                return redirect('profile') 
            else:
                messages.error(request, 'Invalid username or password!')    
    return  login_form

# from django.contrib.auth.views import LoginView as DjangoLoginView
# from django.urls import reverse_lazy

# class LoginView(DjangoLoginView):
#     template_name = "profile.html"
#     success_url = reverse_lazy("accounts:profile")

@login_required
def profile_view(request):
    user = request.user
    print(user)
    return render(request, 'profile.html')


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def auth_settings_view(request):
    login(request)
    return render(request, 'auth_settings.html')