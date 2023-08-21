from django.db import models

# Create your models here.
class Event(models.Model):
  date = models.DateField()
  location = models.CharField(max_length=255)
  venue = models.CharField(max_length=255)

  def __str__(self):
        return f"{self.date} - {self.location}, {self.venue}"