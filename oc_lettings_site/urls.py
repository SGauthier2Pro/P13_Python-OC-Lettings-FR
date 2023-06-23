from django.contrib import admin
from django.urls import path, include

from .views.index import index
from .views.not_found import not_found

urlpatterns = [
    path('', index, name='index'),
    path(r'lettings/', include('lettings.urls', namespace='lettings')),
    path(r'profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
