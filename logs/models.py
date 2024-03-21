from django.db import models
from django.utils import timezone


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Record(models.Model):
    name = models.CharField(max_length=100)
    items = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(default=timezone.now)
    date_returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.department.name}"
