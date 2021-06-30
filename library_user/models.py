from django.contrib.auth.models import User
from django.db import models

USER_TYPE = (
    ('STUDENT', 'STUDENT'),
    ('LIBRARIAN', 'LIBRARIAN'),
)


class LibraryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(choices=USER_TYPE, max_length=13, default='STUDENT')
    student_id = models.CharField(max_length=10, blank=True, null=True)
    staff_id = models.CharField(max_length=10, blank=True, null=True)
    department = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + self.user.last_name