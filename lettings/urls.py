from django.urls import path
from .views import index, letting


app_name = 'lettings'
urlpatterns = [
    path('', index, name='lettings_index'),
    path('<int:letting_id>/', letting, name='letting'),
]
