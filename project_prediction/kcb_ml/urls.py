from django.conf.urls import url
from kcb_ml import views

urlpatterns = [
    url(r'^api/kcb_ml_view$', views.kcb_ml_list),
    url(r'^api/kcb_ml_pred$', views.kcb_ml_pred),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]
