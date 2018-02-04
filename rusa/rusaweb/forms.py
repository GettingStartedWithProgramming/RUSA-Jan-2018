from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import (
	Participant,
)

# full_name = forms.CharField(required=True)
# is_student = forms.BooleanField()
# college_name = forms.CharField(max_length=350)
# AGE_GROUP_CHOICES = (
# 	('AA', "10-14"),
# 	('AB', "15-18"),
# 	('BB', "19-23"),
# 	('BC', "Above 23"),
# )
# age_group = forms.CharField(max_length=2, choices=AGE_GROUP_CHOICES)


class UserSignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class ParticipantSignupForm(forms.ModelForm):
	class Meta:
		model = Participant
		fields = ('full_name', 'is_student', 'college_name', 'age_group', 'program')
