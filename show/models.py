from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserDetails(models.Model):
    user_data = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10, null=True)
    last_name = models.CharField(max_length=10, null=True)
    mobile = models.IntegerField(null=True, default=0000000000)
    gender = models.CharField(max_length=10, null=True)
    age = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.first_name
