from django.db import models
from django.conf import settings
# Create your models here.

class Category(models.Model):
    CATEGORIES_CHOICES = (
        ('ecommerce', 'Ecommerce'),
        ('digital', 'Digital'),
        ('restaurant', 'Restaurant'),
    )
    type = models.CharField(max_length=20, choices=CATEGORIES_CHOICES)
    

    def __str__(self):
        return self.type


class Business(models.Model):
    STATUS_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
    )

    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    seller = models.CharField(max_length=255)
    email = models.EmailField()
    number = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    location = models.CharField(max_length=255)
    price = models.IntegerField()
    revenue = models.IntegerField()
    expense = models.IntegerField()
    profit = models.IntegerField()
    description = models.TextField(max_length=2000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    img1 = models.CharField(max_length=255)
    img2 = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    business = models.CharField(max_length=255)
    seller = models.CharField(max_length=255)
    businessprice = models.IntegerField()
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    introduction = models.TextField(max_length=1000)
    number = models.IntegerField()
    tokenpaid = models.IntegerField()

    def __str__(self):
        return self.business + ' being purchased by ' + self.username


