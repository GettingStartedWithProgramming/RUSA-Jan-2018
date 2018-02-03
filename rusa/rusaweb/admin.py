from django.contrib import admin
from .models import (
	Program,
	Participant,
	Task,
	TaskCompletion,
)
# Register your models here.

admin.site.register(Program)
admin.site.register(Participant)
admin.site.register(Task)
admin.site.register(TaskCompletion)
