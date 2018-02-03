from django.contrib import admin
from .models import (
	Program,
	Participant,
	Task,
	TaskCompletion,
)
# Register your models here.

class ProgramAdmin(admin.ModelAdmin):
	list_display = ["name", "start_date", "no_of_registrations", "no_of_tasks", "end_date"]
	class Meta:
		model = Program

class ParticipantAdmin(admin.ModelAdmin):
	list_display = ["user_name", "email", "age_group", "program"]
	class Meta:
		model = Participant

class TaskAdmin(admin.ModelAdmin):
	list_display = ["name", "start_date", "no_of_submissions", "program"]
	class Meta:
		model = Task

class TaskCompletionAdmin(admin.ModelAdmin):
	list_display = ["task", "participant", "completion_date"]
	class Meta:
		model = TaskCompletion

admin.site.register(Program, ProgramAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskCompletion, TaskCompletionAdmin)
