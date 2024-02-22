from django.shortcuts import render, redirect
from django.views.generic import View
from blog.forms import BlogForm


class HomePageView(View):
    template_name = 'blog/home.html'

    def get(self, request):
        return render(request, self.template_name)


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

        return render(request, self.template_name, {'form': form})
