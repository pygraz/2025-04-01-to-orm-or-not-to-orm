# Copyright (c) 2025 Python User Group Graz. Distributed under the MIT license.
from django.contrib.auth.models import User
from django.db import models


class IssueState(models.TextChoices):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"


class Label(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Issue(models.Model):
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="issues")
    labels = models.ManyToManyField(Label, related_name="issues")

    title = models.CharField(max_length=100)
    state = models.CharField(choices=IssueState, default=IssueState.TODO)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title
