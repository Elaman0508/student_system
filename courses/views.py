from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_create(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('course_list')
    return render(request, 'courses/course_form.html', {'form': form})
