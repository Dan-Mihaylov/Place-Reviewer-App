from django.contrib.auth import login, authenticate
from django.shortcuts import render, HttpResponse, redirect

from TheReviewApp.accounts.forms import RegisterUserForm, CustomAuthenticationForm


def register_page(request):

    if request.method == 'POST':
        form = RegisterUserForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('place_add')

    form = RegisterUserForm()

    return render(request, template_name='accounts/register.html', context={'form': form})


def login_page(request):

    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                print('yeah')
                print(form.get_user())
                login(request, user)
                return redirect('login')

    form = CustomAuthenticationForm()
    return render(request, template_name='accounts/login.html', context={'form': form})

