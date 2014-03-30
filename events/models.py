from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	link = models.URLField(max_length=200, blank=True)
	banner = models.FileField(upload_to='banners/', blank=True)
	start = models.DateTimeField()
	end = models.DateTimeField()
	description = models.TextField()
	age = models.IntegerField()
	tip = models.IntegerField()
	going = models.ManyToManyField(User, blank=True)
	def tipped(self):
		if len(self.going.all()) >= self.tip:
			return True
		else:
			return False
	tipped.boolean = True
	def __unicode__(self):
		return self.title