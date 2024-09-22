from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import IdeaSubmissionForm

# Create your views here.
def ideaform(request):
    if request.method == 'POST':
        form = IdeaSubmissionForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = IdeaSubmissionForm()

    return render(request, 'submit_idea.html', {'form': form})