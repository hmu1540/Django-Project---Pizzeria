from django import forms
from django.forms import fields
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'pizza']
        labels = {'name': ''} #??????????????????????????????????

        widgets = {'name': forms.Textarea(attrs={'cols': 40})}  # custom fields