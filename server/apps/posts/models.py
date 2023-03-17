from django.db import models

class User(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField(default=0)

class Post(models.Model):
    title = models.CharField(max_length=64)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="post_user") 
    content = models.TextField()
    region = models.CharField(max_length=16)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, upload_to='posts/%Y%m%d')

