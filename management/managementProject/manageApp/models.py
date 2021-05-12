from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name= models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    district= models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    memo = models.TextField(default="메모 없음")
    
    def __str__(self):
        return self.district + self.price + self.area +  self.owner  + self.date

    def get_absolute_url(self):
        return reverse('home')


class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)
 