from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {
            'title': forms.TextInput(attrs={'class': 'title'}),
            'text': forms.TextInput(attrs={'class': 'text'}),
        }