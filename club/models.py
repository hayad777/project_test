
from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3)
    membership_id = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='member_photos/', blank=True, null=True)

    def __str__(self):
        return self.name



