from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import (
	UserSignupForm,
	ParticipantSignupForm,
)
from .models import (
	Program,
	Participant,
)

# Create your views here.

login_url = "/signup"

def home(request):
	return render(request, "home.html", {})

def signupForm(request):
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
	# This is hash password(encoded password)
	raw_password = userform.cleaned_data.get('password1')
	user = authenticate(username=user.username, password=raw_password)
	login(request, user)
	return redirect("/account/")

@login_required(login_url=login_url)
def userAccount(request):
	participant = get_object_or_404(Participant, user=request.user)
	return render(request, "account.html", {"participant": participant})
