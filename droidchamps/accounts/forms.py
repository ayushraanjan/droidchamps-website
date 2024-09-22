# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('mentor', 'Mentor'),
        ('student', 'Student'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('user_type', 'profile_picture',)