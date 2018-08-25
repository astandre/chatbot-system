from django.urls import path
from django.conf.urls import url
from nluengine import views

urlpatterns = [
    path(r'search/', views.search_bar, name='search'),
    url(r'resolve=(?P<query>[0-9a-zA-Z\+]+)$', views.nlu_engine, name='resolve'),
]
