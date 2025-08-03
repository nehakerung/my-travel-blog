from django.http import HttpResponse
from django.shortcuts import render

from .models import Trip

# Create your views here.


def trips_page(request):
    # return render(request, "basic.html")
    return render(request, "trip_page.html")

    # if Trip:
    #     posts = Trip.objects.all()
    #     return render(request, "templates/trips_page.html", {"posts": posts})
    # else:
