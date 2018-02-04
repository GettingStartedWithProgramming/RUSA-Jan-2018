from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Program(models.Model):
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=1000, default="", blank=True)
	start_date = models.DateField()
	end_date = models.DateField()
	no_of_registrations = models.PositiveIntegerField(default=0, blank=True)
	no_of_tasks = models.PositiveIntegerField(default=0, blank=True)

	def __str__(self):
		return self.name

class Participant(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	program = models.ForeignKey(Program, on_delete=models.PROTECT)
	full_name = models.CharField(max_length=100)
	is_student = models.BooleanField(default=False)
	college_name = models.CharField(max_length=350, default="", blank=True)
	AGE_GROUP_CHOICES = (
		('AA', "10-14"),
		('AB', "15-18"),
		('BB', "19-23"),
		('BC', "Above 23"),
	)
	age_group = models.CharField(max_length=2, choices=AGE_GROUP_CHOICES, default='AB')
	joined_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user_name + " : " + self.email

class Task(models.Model):
	program = models.ForeignKey(Program, on_delete=models.PROTECT)
	name = models.CharField(max_length=400)
	description = models.CharField(max_length=1500)
	start_date = models.DateTimeField(auto_now_add=True)
	no_of_submissions = models.PositiveIntegerField(default=0, blank=True)

	def __str__(self):
		return self.name + " : " + str(self.no_of_submissions)

class TaskCompletion(models.Model):
	participant = models.ForeignKey(Participant, on_delete=models.PROTECT)
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	completion_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.task.name) + " : " + str(self.participant.email)
