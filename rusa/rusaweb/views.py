from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import (
	UserSignupForm,
	ParticipantSignupForm,
)
from .models import (
	Program,
	Participant,
	Task,
	TaskCompletion,
)

# Create your views here.
login_url = "/signup/"
PROGRAM_NAME = "RUSA 2018"

def home(request):
	program = get_object_or_404(Program, name=PROGRAM_NAME)
	return render(request, "home.html", {"program": program})

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
	return redirect("/accounts/profile/")

@login_required(login_url=login_url)
def userAccount(request):
	participant = get_object_or_404(Participant, user=request.user)
	return render(request, "account.html", {"participant": participant})

@login_required(login_url=login_url)
def logoutUser(request):
	logout(request)
	return home(request)

@login_required(login_url=login_url)
def listTasks(request):
	participant = get_object_or_404(Participant, user=request.user)
	tasks = Task.objects.filter(program=participant.program)
	return render(request, "tasks.html", {"tasks": tasks})

@login_required(login_url=login_url)
def listCompletedTasks(request):
	participant = get_object_or_404(Participant, user=request.user)
	tasks = TaskCompletion.objects.filter(program=participant.program)
	return render(request, "tasks.html", {"tasks": tasks})

@login_required(login_url=login_url)
def getTask(request, task_id):
	participant = get_object_or_404(Participant, user=request.user)
	task = Task.objects.get(program=participant.program, id=task_id)
	submissions = TaskCompletion.objects.filter(task=task)
	return render(request, "task.html", {"task": task, "submissions": submissions})

@login_required(login_url=login_url)
def getTask(request, task_id):
	participant = get_object_or_404(Participant, user=request.user)
	task = Task.objects.get(program=participant.program, id=task_id)
	submissions = TaskCompletion.objects.filter(task=task)
	return render(request, "task.html", {"task": task, "submissions": submissions})

@login_required(login_url=login_url)
def getUser(request, user_id):
	participant = get_object_or_404(Participant, user=request.user)
	user = get_object_or_404(Participant, id=user_id, program=participant.program)
	tasks = TaskCompletion.objects.filter(participant=user)
	return render(request, "user.html", {"user": user, "tasks": tasks})

@login_required(login_url=login_url)
def getAllUsers(request):
	participant = get_object_or_404(Participant, user=request.user)
	users = Participant.objects.filter(program=participant.program)
	return render(request, "users.html", {"users": users})
