from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    template_name = 'users/register.html'

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login in!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, template_name, {'form': form})
