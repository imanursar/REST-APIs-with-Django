from django.conf.urls import url
from kcb_ml import views
from django.urls import path, re_path

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    url(r'^api/kcb_ml_view$', views.kcb_ml_view.as_view()),
    # path('api/kcb_ml_view', views.kcb_ml_view.as_view()),
    url(r'^api/kcb_ml_pred$', views.kcb_ml_pred.as_view()),

    url(r'^api/kcb_ml_list$', views.userview.as_view()),

    url(r'^api/users$', views.userview_feature.as_view()),

    url(r'^api/users/search$', views.searchuserview.as_view()),

    url(r'^api/users/(?P<user_id>[0-9]+)$', views.useridview.as_view()),

    # Paths for login
    re_path(r'^login(?:\/)?$', views.Login.as_view()),
    re_path(r'^login/refresh(?:\/)?$', views.LoginRefresh.as_view()),
    path('login/register', views.Register.as_view()),


    url(r'^about/', views.contact.as_view()),
    # url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    # url(r'^api/tutorials/published$', views.tutorial_list_published)
]
