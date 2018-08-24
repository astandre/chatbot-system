from django.urls import path

from nluengine import views

urlpatterns = [
    path(r'test/', views.nlu_engine, name='test'),

]
