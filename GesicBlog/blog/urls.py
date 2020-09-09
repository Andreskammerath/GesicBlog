from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('article/<int:identificador>/', views.article, name='article')

]