from django import forms
from .models import Idea

class IdeaSubmissionForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'student_name', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }