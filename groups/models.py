from django.db import models

from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.faculty})"
