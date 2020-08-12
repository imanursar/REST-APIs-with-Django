# from django.shortcuts import render

# Create your views here.
# howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"

#I did not define a get method. This is just another way of using the TemplateView
# class. If you set the template_name attribute, a get request to that view will
# automatically use the defined template. Try changing the HomePageView to use
# the format used in AboutPageView.
