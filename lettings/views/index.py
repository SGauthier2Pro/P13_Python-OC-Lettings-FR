from django.shortcuts import render
from lettings.models.letting import Letting


def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)
