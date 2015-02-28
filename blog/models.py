from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100, unique=True)
	# slug generates a valud URL
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	tag = models.ForeignKey('blog.Tag')

	def __str__(self):
		return self.title


class Tag(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	created = models.DateField(db_index=True, auto_now_add=True)
	author = models.CharField(max_length=60)
	body = models.TextField()
	post = models.ForeignKey(Post)

	def __str__(self):
		return self.body
