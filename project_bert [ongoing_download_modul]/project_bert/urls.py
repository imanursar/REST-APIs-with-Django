"""project_bert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
        # Adding a new URL
    path('model/', views.call_model.as_view())
]

# Here, we use as as_view function because in Class-based views,
# we have to call as_view() function so as to return a callable view
# that takes a request and returns a response.
# Its the main entry-point in request-response cycle in case of generic views.
# as_view is the function(class method) which will connect our call_model class with its url.
