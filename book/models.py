from django.db import models

from student.models import Student


class BookCategory(models.Model):
    category_name = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class Book(models.Model):

    title = models.CharField(max_length=40,)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    author = models.CharField(max_length=40)
    date_published = models.DateField()
    number_of_pages = models.IntegerField()
    inventory = models.IntegerField()

    def __str__(self):
        return self.title


class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)
    expected_return = models.DateField()

    def __str__(self):
        return self.book.title