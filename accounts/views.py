from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpRequest

# Custom Login View
def my_custom_login_view(request: HttpRequest):
    # Warning message for already logged-in users
    warning_message = ''
    
    if request.user.is_authenticated:
        warning_message = 'You are already logged in.'
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('some_success_url')  # Update this to your success URL
        else:
            form = AuthenticationForm()

    context = {
        'form': form,
        'warning_message': warning_message,
    }
    return render(request, 'auth/login.html', context)

# Success View
def success_view(request):
    return redirect('home')

# Custom Logout View
def my_custom_logout_view(request: HttpRequest):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have successfully logged out.')
    return redirect('home')
