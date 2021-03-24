from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class Demo(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    status = models.BooleanField(default=False)
    mobile_no = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])
    image = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return self.name