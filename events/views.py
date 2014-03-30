from django.shortcuts import render, get_object_or_404
from events.models import Event
from events.forms import EventForm
from allauth.socialaccount.views import SignupView

# Create your views here.
def index(request):
	return render(request, 'events/index.html')

def create(request):
	form = EventForm()
	return render(request, 'events/create.html', { 'form': form })

def detail(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	return render(request, 'events/detail.html', { 'event': event })

class PrettySignupView(SignupView):
	template_name = 'events/signup.html'
	def form_valid(self, form):
		return super(SignupView, self).form_valid(form)

signup = PrettySignupView.as_view()