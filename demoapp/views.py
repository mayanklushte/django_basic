from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView
from .models import *
from django.contrib.auth.models import User
from .forms import *
# Create your views here.


def index(request):
    data = Demo.objects.filter(user__user_id=request.user)

    return render(request, 'index.html', {'data': data})


def details(request, id):
    data = Demo.objects.get(id=id)
    return render(request, 'contact.html', {'data': data})


def delete(request, id):
    data = Demo.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('demoapp:index'))


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
            form_r.is_customer = True
            form_r.save()
            return HttpResponseRedirect(reverse('demoapp:index'))

        else:
            print(form_p.errors, form.errors)
    else:
        form = UserForm()
        form_p = UserRegisterForm()

    return render(request, 'user_register.html', {'form': form, 'form_p': form_p})


def register_shop(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        form_p = ShopRegisterForm(request.POST, request.FILES)
        if form.is_valid() and form_p.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            form_r = form_p.save(commit=False)
            form_r.user = user  # here connected OneToOneField with user table
            form_r.is_shop = True
            form_r.save()
            return HttpResponseRedirect(reverse('demoapp:index'))

        else:
            print(form_p.errors, form.errors)
    else:
        form = UserForm()
        form_p = ShopRegisterForm()

    return render(request, 'shop_register.html', {'form': form, 'form_p': form_p})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                try:
                    data = UserRegister.objects.get(user_id=user)
                    if data.is_customer == True:
                        login(request, user)
                        return HttpResponseRedirect(reverse('demoapp:index'))
                except:
                    data2 = ShopRegister.objects.get(user_id=user)
                    if data2.is_shop == True:
                        login(request, user)
                        return HttpResponseRedirect(reverse('demoapp:add_demo'))
            else:
                print('user is not active')
        else:
            messages.info(request, 'Username or password is wrong!')
            return HttpResponseRedirect(reverse('demoapp:login'))
    else:
        return render(request, 'login.html')


class DemoList(ListView):
    model = Demo
    template_name = 'class_list.html'
    context_object_name = 'data'


def update_demo(request, id):
    instance = Demo.objects.get(id=id)
    form = DemoForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('demoapp:index'))
    else:
        print(form.errors)
    return render(request, 'update_demo.html', {'form': form})
