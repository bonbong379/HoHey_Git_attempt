from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class film_profile(models.Model):
	film_name= models.CharField(max_length=100, unique=True)
	film_summary = models.TextField()
	film_image = models.ImageField(default='default.jpg', upload_to='film_profile')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.film_name

	def get_absolute_url(self):
		return reverse('film-home', kwargs={'filmid': self.pk})
	
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.film_image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.film_image.path)

class Review(models.Model):
    master = models.ForeignKey(film_profile, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.content

class Essay(models.Model):
    master = models.ForeignKey(film_profile, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.content

class Comment(models.Model):
    film_master = models.ForeignKey(film_profile, on_delete = models.CASCADE)
    master = models.ForeignKey(Essay, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(default = timezone.now)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete = models.CASCADE, null=True, related_name='child')

    def __str__(self):
        return self.content