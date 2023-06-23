from django.shortcuts import render
from profiles.models.profile import Profile


def profile(request, username):
    if Profile.objects.filter(user__username=username):
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    else:
        return render(request, 'not_found.html')
