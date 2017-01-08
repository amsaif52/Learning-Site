from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    output = ', '.join([str(course) for course in courses])
    return HttpResponse(output)
