from django.shortcuts import render
from django.views.generic import View

class HomePageView(View):
    template_name = 'blog/home.html'

    def get(self, request):
        return render(request, self.template_name)


