from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'demoapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('user_register', views.register_user, name="user_register"),
    path('add_demo/', views.add_demo, name="add_demo"),
    path('login', views.user_login, name="login"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)