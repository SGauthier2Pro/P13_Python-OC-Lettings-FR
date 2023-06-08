from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(r'lettings/', include('lettings.urls', namespace='lettings')),
    path(r'profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
