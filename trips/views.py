from django.http import HttpResponse
from django.template import loader

from .models import Trip


def trips_page(request):
    """At the moment - returns a basic html page."""
    trips = Trip.objects.all().values()
    template = loader.get_template("trip_page.html")
    context = {
        "trips": trips,
    }
    return HttpResponse(template.render(context, request))
