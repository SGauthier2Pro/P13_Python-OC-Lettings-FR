from django.contrib import admin
from django.urls import path, include

from .views.index import index

urlpatterns = [
    path('', index, name='index'),
    path(r'lettings/', include('lettings.urls', namespace='lettings')),
    path(r'profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
