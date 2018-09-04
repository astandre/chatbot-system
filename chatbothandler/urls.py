from django.urls import path
from chatbothandler import views
from django.conf.urls import url


urlpatterns = [
    # path(r'search/', views.search_bar, name='search'),
    # path(r'upload/', views.upload_file, name='upload_file'),
    # path(r'knowledge/', views.knowledge, name='knowledge'),
    path(r'user/new/', views.new_user, name='new_user'),
    path(r'user/input/', views.new_input, name='new_input'),
    # url(r'resolve=(?P<query>[0-9a-zA-Z\+]+)$', views.nlu_engine, name='resolve'),
]
