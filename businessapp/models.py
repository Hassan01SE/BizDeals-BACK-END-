from django.db import models

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
    id = models.AutoField(primary_key=True)
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
    img1 = models.CharField(max_length=255)
    img2 = models.CharField(max_length=255)

    def __str__(self):
        return self.title
