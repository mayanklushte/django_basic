from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserRegister(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])
    Address = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pic')
    is_customer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name


class ShopRegister(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])
    Address = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pic')
    shop_name = models.CharField(max_length=120)
    is_shop = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name


class Demo(models.Model):
    user = models.ForeignKey(UserRegister, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    status = models.BooleanField(default=False)
    mobile_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])
    image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return self.name