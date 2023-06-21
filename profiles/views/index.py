from django.shortcuts import render
from profiles.models.profile import Profile


def index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)
