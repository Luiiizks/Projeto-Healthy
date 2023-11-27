from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.models import User

class SignUp(View):
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, self.template_name)

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        messages.success(request, 'Registration successful. You are now logged in.')
        return redirect('login')
