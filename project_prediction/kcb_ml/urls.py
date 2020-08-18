from django.conf.urls import url
from kcb_ml import views
from django.urls import path

urlpatterns = [
    url(r'^api/kcb_ml_view$', views.kcb_ml_list),
    url(r'^api/kcb_ml_pred$', views.kcb_ml_pred),
    url(r'^api/kcb_ml_list$', views.userview),
    url(r'^api/users/search$', views.searchuserview),
    # path('api/users/search', views.searchuserview, name='searchuserview'),
    url(r'^api/users$', views.userview_feature),
    # path('api/users/', views.userview_feature, name='userview_feature'),
    url(r'^api/users/(?P<user_id>[0-9]+)$', views.useridview),
    # path('api/users/<user_id>', views.useridview, name='useridview'),

    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]
