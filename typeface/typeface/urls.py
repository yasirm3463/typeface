"""
URL configuration for typeface project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('files/upload/', views.upload_file),
    path('files/<uuid:file_id>/', views.read_file),
    path('files/<uuid:file_id>/', views.update_file),
    path('files/<uuid:file_id>/', views.delete_file),
    path('files/', views.list_files),
]
