from django.db import models
from django.contrib.auth.models import User


class User_login(models.Model):
	user = models.OneToOneField(
		to=User, on_delete=models.CASCADE
	)
	email = models.EmailField(blank=True, null=True)

	def __str__(self):
		return self.name
        