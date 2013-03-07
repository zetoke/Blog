from django.db import models
from django.db.models import permalink

# Create your models here.
class Posts(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)
	body = models.TextField()
	posted = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey('blog.Category')

	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_post', None, {'slug': self.slug})

class Category(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)

	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_category', None, { 'slug': self.slug})