from django.db import models


class Enroll(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=32)
    course = models.CharField(max_length=20)
    shift = models.CharField(max_length=15)
    address = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    contact_no = models.CharField(max_length=14)

    def __str__(self):
        return self.name
