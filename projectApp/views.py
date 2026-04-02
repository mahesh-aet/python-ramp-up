from datetime import date

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from projectApp.models import Album

# Create your views here.
def index(request):
    try:
        # album = Album.objects.get(name="hero album")
        album = Album.objects.filter(release_date__gt = date(2026, 3, 1))
    except Album.DoesNotExist:
        print("album doesn't exit")
        return HttpResponse("album doesn't exit")
    except Album.MultipleObjectsReturned:
        print("multiple albums exists")
        return HttpResponse("multiple albums exists")
    return JsonResponse(list(album.values()),safe=False)


def simple_view(request):
    context = {"data":"GFG is the best"}
    return render(request, "simple.html",context)

def check_age(request):
    age = None
    if(request.method == 'POST'):
        age = int(request.POST.get('age',0))
    return render(request, 'check_age.html',{'age':age})

def loop(request):
    data = "GFG is the best"
    number_list = [1,2,3,4]
    context = {
        "data":data,
        "list":number_list
    }
    return render(request, 'loop.html', context)



