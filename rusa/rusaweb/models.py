from django.db import models

# Create your models here.

class Program(models.Model):
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=1000, default="", blank=True)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	no_of_registrations = models.PositiveIntegerField()
	no_of_tasks = models.PositiveIntegerField()

class Participant(models.Model):
	program = models.ForeignKey(Program, on_delete=models.PROTECT)
	email = models.EmailField(max_length=50, unique=True)
	user_name = models.CharField(max_length=25, unique=True)
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
	joined_data = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
	program = models.ForeignKey(Program, on_delete=models.PROTECT)
	name = models.CharField(max_length=400)
	description = models.CharField(max_length=1500)
	start_date = models.DateTimeField(auto_now_add=True)
	no_of_submissions = models.PositiveIntegerField()

class TaskCompletion(models.Model):
	participant = models.ForeignKey(Participant, on_delete=models.PROTECT)
	task = models.ForeignKey(Task, on_delete=models.CASCADE)
	completion_date = models.DateTimeField(auto_now_add=True)
