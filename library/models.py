from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(max_length=50)


class Purchase(models.Model):
    book = models.ManyToManyField(Book)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
