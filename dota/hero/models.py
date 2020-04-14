from django.db import models

# Create your models here.
class BannerHome(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BannerAbout(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Team(models.Model):
    first_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    bod = models.DateField(auto_now=True)
    address =  models.TextField()
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    education = models.TextField()
    experience = models.TextField()

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    

class Comment(models.Model):
    username = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    message = models.TextField()