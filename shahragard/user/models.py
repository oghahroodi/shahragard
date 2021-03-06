from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=100, null=False)
    # phone_regex = RegexValidator(
    #     regex=r'^\+?1?\d{10,11}$',
    #     message="شماره تلفن باید عدد و بین 10 تا 11 رقم باشد.")
    phone_number = models.CharField(max_length=100, unique=True, null=False)
    validation = models.BooleanField(default=False)
    account_creation_date = models.DateTimeField(
        'date published', default=timezone.now)
    # email_regex = RegexValidator(
    #     regex=r"[^@]+@[^@]+\.[^@]+", message="فرمت ایمیل اشتباه است.")
    email = models.CharField(max_length=70, null=False, unique=True)
    car = models.CharField(max_length=10, null=True, blank=True)
    plaque = models.CharField(max_length=5, null=True, blank=True)

    def hasCar(self):
        if self.car is not None and self.plaque is not None:
            return True


class SuggetionFeature(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mashhad = models.IntegerField(null=False, default=0)
    tehran = models.IntegerField(null=False, default=0)
    karaj = models.IntegerField(null=False, default=0)
    shiraz = models.IntegerField(null=False, default=0)
    qom = models.IntegerField(null=False, default=0)
    search_origin_count = models.IntegerField(null=False, default=0)
    search_des_count = models.IntegerField(null=False, default=0)
    make_trip_count = models.IntegerField(null=False, default=0)
