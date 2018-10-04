from django.urls import path
from nluengine import views

urlpatterns = [
    path(r'search/', views.search_bar, name='search'),
    path(r'upload/', views.upload_file, name='upload_file'),
    path(r'knowledge/', views.knowledge, name='knowledge'),
    path(r'api/knowledge/', views.knowledge_api, name='knowledge_api'),
    path(r'resolve/', views.nlu_engine, name='resolve'),
]
