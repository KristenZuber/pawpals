from django.db import models
from django.contrib.auth.models import User

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.User.username} Account Info'

# Model for the application
class Apply(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    phone_number = models.IntegerField()
    answer1 = models.CharField(max_length = 100)
    answer2 = models.IntegerField()
    answer3 = models.IntegerField()

    def __str__(self):
        return self.first_name
