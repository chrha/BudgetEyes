from django.db import models

# Create your models here.

class Currency(models.Model):
  name = models.CharField(max_length=50)
  value = models.IntegerField(default=0)

  def __str__(self):
    return "{}, current value is: {}".format(self.name, self.value)