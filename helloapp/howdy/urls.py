# howdy/urls.py
from django.conf.urls import url
from howdy import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
]
