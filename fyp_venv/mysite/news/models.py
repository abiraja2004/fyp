from django.db import models
from django.core import urlresolvers

# Create your models here.
class Post(models.Model):
	category = models.CharField(blank=True, max_length=100)
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	fivelinesummary = models.TextField(blank=True)
	tenlinesummary = models.TextField(blank=True)
	sum_basic = models.TextField(blank=True)
	LSA = models.TextField(blank=True)
	textrank = models.TextField(blank=True)
	lexrank = models.TextField(blank=True)
	featured_lexrank = models.TextField(blank=True)	
	photo = models.URLField(blank=True)
	location = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	link = models.URLField(blank=True)
	pub_date = models.DateTimeField()
	def __str__(self):
		return self.title
	def get_absolute_url(self):
                return urlresolvers.reverse('post_detail', args=[self.pk])

class Quotation(models.Model):
	post = models.ForeignKey(Post, related_name='quotation')
	quotation = models.TextField(blank=True)
	speaker = models.TextField(blank=True)
	date = models.DateTimeField()
	def __str__(self):
		return self.quotation