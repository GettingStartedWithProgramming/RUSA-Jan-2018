from django.shortcuts import render
from django.http import HttpResponse
from .forms import (
	UserSignupForm,
	ParticipantSignupForm,
)
from .models import Program

# Create your views here.

def home(request):
	return render(request, "home.html", {})

def signup(request):
	if request.method == 'POST':
		userform = UserSignupForm(request.POST)
		pform = ParticipantSignupForm(request.POST)
		if userform.is_valid() and pform.is_valid():
			return signupUser(request)
	else:
		userform = UserSignupForm()
		pform = ParticipantSignupForm()
	return render(request, "signup.html", {'userform': userform, 'pform': pform})

def signupUser(request):
	userform = UserSignupForm(request.POST)
	pform = ParticipantSignupForm(request.POST)
	user = userform.save(commit=True)
	participant = pform.save(commit=False)
	participant.user = user
	participant.save()
	program = Program.objects.get(name=participant.program)
	program.no_of_registrations += 1
	program.save()
	return HttpResponse("Hello, " + str(user))
