from django.shortcuts import render
from .models import Resource

def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'resource_list.html', {'resources': resources})