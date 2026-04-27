from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import *

class create_post_form(forms.Form):
    title = forms.CharField(max_length=69)
    content = forms.CharField()

    class Meta:
        model = Post
        fields = ['title', 'content']

class update_post_form(forms.Form):
    title = forms.CharField(max_length=69)
    content = forms.CharField()

    class Meta:
        model = Post
        fields = ['title', 'content']

class comment_form(forms.Form):
    comment = forms.CharField()

    class Meta:
        model = Comment
        fields = ['comment']