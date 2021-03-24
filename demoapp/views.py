from django.shortcuts import render
from django.http import HttpResponse
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


