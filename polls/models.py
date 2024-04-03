from django.db import models
from django.utils import timezone

class Question(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Choice(models.Model):
    category = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
