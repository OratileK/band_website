from django.db import models

# Create your models here.
class oneEvent(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} - {self.location}, {self.venue}"
