from django.contrib.auth.models import User
from django.db import models


class LibraryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + self.user.last_name