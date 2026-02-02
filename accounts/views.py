"""
Authentication views: register, login, logout.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from .forms import UserRegisterForm, UserLoginForm


@require_http_methods(['GET', 'POST'])
def register_view(request):
    if request.user.is_authenticated:
        return redirect('courses:course_list')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('courses:course_list')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.user.is_authenticated:
        return redirect('courses:course_list')
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next') or reverse('courses:course_list')
            return redirect(next_url)
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def logout_view(request):
    logout(request)
    return redirect('courses:course_list')
