from django.db import models


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