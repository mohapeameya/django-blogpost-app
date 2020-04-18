from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	"""docstring for Post"""

	title 				= models.CharField(max_length=100)
	content 			= models.TextField()
	date_posted 		= models.DateTimeField(default=timezone.now)
	author 				= models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	
	# ImproperlyConfigured at /post/new/
	# No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
	# after creating a post the PostCreateView doesn't know where to redirect
	def get_absolute_url(self):
		# not using redirect because it will redirect to a specific route whereas
		# reverse returns the full url for the route as a string
		return reverse('post-detail', kwargs={'pk': self.pk})

