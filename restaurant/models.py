from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=100)
	user = models.ManyToManyField(User)
	def __str__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	array = models.CharField(max_length=5000, null=True, blank=True)
	
	def __str__(self):
		return self.user.username