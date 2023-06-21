from django.urls import path
from lettings.views.index import index
from lettings.views.letting import letting


app_name = 'lettings'
urlpatterns = [
    path('', index, name='index'),
    path('<int:letting_id>/', letting, name='letting'),
]
