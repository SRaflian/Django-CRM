from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# # Create your views here.
# class UserLoginView(LoginView):
#     template_name = 'accounts/login.html'
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('home')  # Replace 'home' with the name of the URL you want to redirect to after login

# Login 
def my_custom_login_view(request: HttpRequest):
    # Initialize an empty warning message
    warning_message = ''
    
    # Check if the user is already authenticated
    if request.user.is_authenticated:
        # Set a warning message for already logged-in users
        warning_message = 'You are already logged in.'

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if not request.user.is_authenticated:
                    login(request, user)
                    return redirect('record-dashboard')  # Adjust this to where you want to redirect users
                else:
                    warning_message = 'You are already logged in.'
    else:
        form = AuthenticationForm()

    # Include the warning message in the context passed to the template
    context = {
        'form': form,
        'warning_message': warning_message,
    }
    return render(request, 'auth/login.html', context)

# # succes redirect
# def success_view(request):
#     return redirect('record-dashboard')

def my_custom_logout_view(request: HttpRequest):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have successfully logged out.')
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Adjust the redirect as necessary
        else:
            # Handle form errors
            print(form.errors)  # For debugging
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


@login_required  # Ensures that only logged-in users can access this view
def account_details(request):
    user = request.user  # Gets the currently logged-in user
    return render(request, 'auth/details.html', {'user': user})

@login_required
def edit_account(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account_details')  # Redirect to the details view
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'auth/edit-account.html', {'form': form})