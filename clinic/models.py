from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return self.name
