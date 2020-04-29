from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  birth_date = models.DateField(null=True, blank=True)
  bio = models.TextField(max_length=500, blank=True)
  city = models.CharField(max_length=30, blank=True)

# Makes it so that when a user is created, a profile is also created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Budget(models.Model):
  owner = models.OneToOneField(User, related_name='budgetowner', on_delete=models.CASCADE)
  income = models.IntegerField()
  expenses = models.IntegerField()

  def jsonify(self):
    return dict({
      'owner': self.owner.username,
      'income': self.income,
      'expenses': self.expenses
    })

class Stock(models.Model):
  name = models.CharField(max_length=30, unique=True)
  value = models.IntegerField()


