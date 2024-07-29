from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})






def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully','success')
                return redirect('mathematic:index')  # Change 'home' to your desired redirect URL
            else:
                messages.error(request, 'invalid username or password', 'error')
                return redirect('accounts:login')
        else:
            return HttpResponse('Invalid form data.')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})







def logout_view(request):
    logout(request)
    return redirect('accounts:login')  # Change 'login' to your desired redirect URL after logout
