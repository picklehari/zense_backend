from django.conf.urls import url
from testApps import views

urlpatterns = [
    url(r'^apps/$', views.applist),
    url(r'^apps/(?P<pk>[a-z]+)/$', views.appDetails),
]