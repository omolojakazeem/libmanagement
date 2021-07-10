from django.db import models

SEX = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
)


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    sex = models.CharField(choices=SEX, max_length=6)
    student_id = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + self.last_name