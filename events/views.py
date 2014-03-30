from django.shortcuts import render, get_object_or_404
from events.models import Event
from events.forms import EventForm

# Create your views here.
def index(request):
	return render(request, 'events/index.html')

def create(request):
	form = EventForm()
	return render(request, 'events/create.html', { 'form': form })

def detail(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	return render(request, 'events/detail.html', { 'event': event })