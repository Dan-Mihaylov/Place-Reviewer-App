from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from django.views import generic as views

from TheReviewApp.accounts.forms import RegisterUserForm, CustomAuthenticationForm, EditAccountForm, EditAccountInfoForm
from TheReviewApp.review.models import Place


def register_page(request):

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account registered for user: {form.cleaned_data["username"]}')
            return redirect('login')
        else:
            messages.error(request, f'{form.errors}')

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


class AccountInfoView(views.ListView, LoginRequiredMixin):
    ITEMS_PER_PAGE = 4

    model = Place
    template_name = 'accounts/account_info.html'
    paginate_by = ITEMS_PER_PAGE

    def get_queryset(self):
        queryset = self.request.user.places.all()
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def account_info(request):
#
#     return render(request, 'accounts/account_info.html')


@login_required(login_url='login')
def edit_account(request):

    if request.method == 'POST':

        edit_account_form = EditAccountForm(request.POST, instance=request.user)
        edit_account_info_form = EditAccountInfoForm(request.POST, request.FILES, instance=request.user.info)

        if edit_account_form.is_valid() and edit_account_info_form.is_valid():
            edit_account_form.save()
            edit_account_info_form.save()
            return redirect('account-info')
    else:
        edit_account_form = EditAccountForm(instance=request.user)
        edit_account_info_form = EditAccountInfoForm(instance=request.user.info)

    context = {
        'account_form': edit_account_form,
        'account_info_form': edit_account_info_form,
    }

    return render(request, 'accounts/edit.html', context=context)


@login_required(login_url='login')
def delete_account(request):

    return HttpResponse('<h1> Delete Account</h1>')
