from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'', include('lettings.urls')),
    path(r'', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
