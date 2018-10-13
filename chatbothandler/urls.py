from django.urls import path
from chatbothandler import views


urlpatterns = [
    path(r'user/new/', views.new_user, name='new_user'),
    path(r'user/input/', views.new_input, name='new_input'),
    path(r'chat/', views.chat, name='chat'),
]
