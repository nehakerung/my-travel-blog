from django.shortcuts import render

# Create your views here.


def trips_page(request):
    """At the moment - returns a basic html page."""
    # return render(request, "basic.html")
    return render(request, "trip_page.html")

    # if Trip:
    #     posts = Trip.objects.all()
    #     return render(request, "templates/trips_page.html", {"posts": posts})
    # else:
