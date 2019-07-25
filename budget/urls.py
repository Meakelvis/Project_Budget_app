from django.contrib import admin
from django.urls import include, path
from . import views
from .views import ProjectCreateView

urlpatterns = [
    path('', views.project_list, name='list'),
    path('add', ProjectCreateView.as_view(), name='add'),
    path('<slug:project_slug>', views.project_detail, name='detail'),
]
