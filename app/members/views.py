from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from members.models import User
from .forms import UserForm, LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('members:index')

    else:
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'members/login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('members:index')
        else:
            return HttpResponse('이미 존재하는 USER 입니다.')
    else:
        form = UserForm()

        context = {
            'form': form,
        }
        return render(request, 'members/signup.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def logout_view(request):
    pass