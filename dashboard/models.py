from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import models

class UserManager(models.Manager):
	pass

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	objects.UserManager()
