from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


from .forms import *
# Create your views here.


def index(request):
    data = Demo.objects.all()
    return render(request, 'index.html', {'data': data})


def contact(request):
    return HttpResponse("contact us")


def add_demo(request):
    if request.method == 'POST':
        form = DemoForm(request.POST, request.FILES)
        if form.is_valid():
            form_r = form.save(commit=False)
            form_r.status = True
            form_r.save()
            return HttpResponse("form submitted")
        else:
            print(form.errors)
    else:
        form = DemoForm()
    return render(request, 'demo.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form_p = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid() and form_p.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            form_r = form_p.save(commit=False)
            form_r.user = user  # here connected OneToOneField with user table
            form_r.save()
            return HttpResponseRedirect(reverse('demoapp:index'))

        else:
            print(form_p.errors, form.errors)
    else:
        form = UserForm()
        form_p = UserRegisterForm()

    return render(request, 'user_register.html', {'form': form, 'form_p': form_p})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('demoapp:index'))
            else:
                print('user is not active')
        else:
            messages.info(request, 'Username or password is wrong!')
            return HttpResponseRedirect(reverse('demoapp:login'))
    else:
        return render(request, 'login.html')
