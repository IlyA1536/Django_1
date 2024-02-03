from django.db import models


class User(models.Model):
    login = models.CharField(max_length=63)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50, choices=[('AD', 'admin'), ('US', 'user')])
    task = models.ManyToManyField("Task")

    def __str__(self):
        return self.login


class Task(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField()
    time_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
