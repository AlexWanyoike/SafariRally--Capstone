from django import forms
from .models import Post , Profile , Comment , Driver , Section, Status 
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm ):
    
    class Meta:
        model = Comment
        fields = ['user', 'post', 'content']

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
        exclude = ['user']

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')