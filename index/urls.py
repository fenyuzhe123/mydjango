from django.urls import path
from . import views

app_name = 'index'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('download/file1', views.download1, name='download1'),
    path('download/file2', views.download2, name='download2')

]