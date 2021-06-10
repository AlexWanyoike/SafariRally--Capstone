from django.db import models
import datetime as dt
from django.contrib.auth.models import User 
from django.db.models.base import Model
from tinymce.models import HTMLField
# Create your models here.

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    name = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to='media/')
    bio = models.TextField(blank=True, max_length=160 )
    contact = models.FloatField(max_length=10 ) 
    email = models.EmailField(blank=False)
    

    def __str__(self):
        return self.user.username

    @classmethod
    def get_profile(cls,username):
        profile = cls.objects.filter(user__username__icontains=username)
        return profile

    @classmethod
    def search_user(cls,username):
        return User.objects.filter(username = username)

class Status(models.Model):
    name = models.CharField(max_length=100  )

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=100  )

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=100  )

    def __str__(self):
        return self.name


class Post(models.Model):
    description = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE , null=True)
    image = models.ImageField(upload_to='media/')
    
    date_posted = models.DateField(null=True, auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.description

    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()
    

    @classmethod
    def get_post_by_user(cls,username):
        post = cls.objects.filter(user__username__contains=username)
        return post 

    class Meta:
        ordering = ['-date_posted']

class Comment(models.Model):
    content = models.TextField(max_length=300)
    date_voted = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.content

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_post_comments(cls,post):
        return cls.objects.filter(post =post)

    class Meta:
        ordering = ['-date_voted']