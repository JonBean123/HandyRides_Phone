from django.shortcuts import render
from django.shortcuts import redirect

from .forms import RideForm, NewRideForm

from .models import Person

# relative import of forms
from .forms import RideForm

# Create your views here.


def index(request):
  context = {}

  possible_entries = ['origination_city', 'origination_state', 'destination_city', 'destination_state', 'date', 'time', 'seats']
  if request.method == 'GET' and any(field in request.GET for field in possible_entries):
      origination_city = request.GET.get('origination_city', '')
      origination_state = request.GET.get('origination_state', '')
      destination_city = request.GET.get('destination_city', '')
      destination_state = request.GET.get('destination_state', '')
      date = request.GET.get('date', '')
      time = request.GET.get('time', '')
      seats = request.GET.get('seats', '')

      context['people'] = Person.objects.filter(
            origination_city__icontains=origination_city,
            origination_state__icontains=origination_state,
            destination_city__icontains=destination_city,
            destination_state__icontains=destination_state,
            date__icontains=date,
            time__icontains=time,
            seats_available__icontains=seats
        )
      return render(request, 'search_results.html', context)

  context['form'] = RideForm()
  return render(request, 'index_view.html', context)

def create(request):
  if request.method == "POST":
    new_ride = NewRideForm(request.POST)
    new_ride.save()
  return redirect("/rides")

def create_rides(request):
  context = {}
  context["new_ride_form"] = NewRideForm()
  return render(request, "create_rides.html",context)


def display_rides(request):
  return render(request, "search_results.html")


