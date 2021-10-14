from django.db.models import F
from django.shortcuts import render
from django.views.generic import  TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.http import HttpResponse , HttpResponseRedirect
from recipes.forms import UserForm, AccountForm


class HomeView(TemplateView):
    template_name = 'recipes/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@login_required
def recipes(request):
    return render(request, 'recipes/recipes.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('recipes:home'))

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('recipes:recipes'))
            else:
                return HttpResponse("Account is not active")
        else:
            return HttpResponse("Invalid credentials")
    else:
        return render(request, 'recipes/login.html')

# class RegisterView(TemplateView):
#     template_name = 'recipes/register.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user_form'] = UserForm()
#         context['acount_form'] = AccountForm()
#         return context

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        acount_form = AccountForm(data=request.POST)

        if user_form.is_valid() and acount_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            account = acount_form.save(commit=False)
            account.user = user

            if 'profile_pic' in request.FILES:
                account.profile_pic = request.FILES['profile_pic']

            account.save()

            registered = True
        else:
            print(user_form.errors, acount_form.errors)
    else:
        user_form = UserForm()
        acount_form = AccountForm()

    return render(request, 'recipes/register.html', {
        'user_form': user_form,
        'acount_form': acount_form,
        'registered': registered
    })