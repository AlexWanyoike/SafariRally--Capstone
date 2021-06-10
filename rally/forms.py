from django import forms
from .models import Post , Profile , Comment , Driver , Section, Status 
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm ):
    
    class Meta:
        model = Comment
        fields = ['user', 'post', 'content', 'date_voted']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile', 'date_posted ' ]

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'profile']