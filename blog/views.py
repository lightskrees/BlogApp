from django.shortcuts import render, redirect
from django.views.generic import View

from authentication.models import User
from blog.forms import BlogForm
from blog.models import Blog


class HomePageView(View):
    template_name = 'blog/home.html'

    def get(self, request):
        blogs = Blog.objects.filter(contributors=request.user)
        return render(request, self.template_name, {'blogs': blogs})


class BlogUploadView(View):
    template_name = 'blog/blog_add.html'
    form_class = BlogForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            blog_form = form.save(commit=False)
            blog_form.contributors = request.user
            blog_form.save()
            return redirect('home')
        else:
            print(form.errors)  # Check for any form validation errors

        return render(request, self.template_name, {'form': form})


class BlogView(View):
    template_name = 'blog/view_blog.html'

    def get(self, request, id):
        blog = Blog.objects.get(id=id)
        return render(request, self.template_name, {'blog': blog})


class UserBlogView(View):
    template_name = 'blog/user_blog.html'

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        blogs = Blog.objects.filter(contributors=user)
        return render(request, self.template_name, {'blogs': blogs})


class UserListView(View):
    template_name = 'blog/users_list.html'

    def get(self, request):
        users = User.objects.all()
        return render(request, self.template_name, {'users': users})
