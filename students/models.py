from django.db import models

from django.db import models
from groups.models import Group

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='students'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    value = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} — {self.value}"
