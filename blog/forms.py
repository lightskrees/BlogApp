from django import forms

from blog.models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['image', 'caption', 'title', 'content']

    def save(self, commit):
        pass