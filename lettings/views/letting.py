from django.shortcuts import render
from lettings.models.letting import Letting


def letting(request, letting_id):
    if str(letting_id).isdigit():
        if Letting.objects.filter(id=letting_id):
            letting = Letting.objects.get(id=letting_id)
            context = {
                'title': letting.title,
                'address': letting.address,
            }
            return render(request, 'lettings/letting.html', context)
        else:
            return render(request, 'not_found.html')
    else:
        return render(request, 'not_found.html')
