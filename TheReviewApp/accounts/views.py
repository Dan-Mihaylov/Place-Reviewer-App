from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from TheReviewApp.accounts.forms import RegisterUserForm, CustomAuthenticationForm


def register_page(request):

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account registered for user: {form.cleaned_data["username"]}')
            return redirect('login')

    form = RegisterUserForm()

    return render(request, template_name='accounts/register.html', context={'form': form})


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Messed Up Something')

    return render(request, template_name='accounts/login.html')


def logout_page(request):

    logout(request)
    return redirect(to='index')
