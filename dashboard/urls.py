from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^clock-in$', views.clock_in),
    url(r'^clock-out$', views.clock_out),
    url(r'^daily-report$', views.daily_report),
]
