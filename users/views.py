# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views import View


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'users/signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después de registrarse
            return redirect('login')  # Redirigir a la página de inicio de sesión o cualquier otra
        return render(request, 'users/signup.html', {'form': form})
