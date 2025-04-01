# Copyright (c) 2025 Python User Group Graz. Distributed under the MIT license.
from django.contrib.auth.models import User
from django.db import models

from django.utils.html import format_html


class IssueState(models.TextChoices):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"


class ROLE_CHOICES(models.TextChoices):
    OWNER = "o", "Owner"
    DEV = "d", "Developer"
    OTHER = "-", "Other"


class Label(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Participant(models.Model):
    issue = models.ForeignKey("Issue", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    def __str__(self):
        return f"Participant {self.id} ({self.role} Issue:{self.issue_id} User:{self.user})"

    def show(self):
        """show self safe for web"""
        return format_html(
            f"<b>{self.user.first_name} {self.user.last_name}</b> has role '<b>{self.get_role_display()}</b>' on Issue '<b>{self.issue}</b>'"
        )


class Issue(models.Model):
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="issues")
    labels = models.ManyToManyField(Label, related_name="issues")
    labels2 = models.ManyToManyField(User, through="Participant")

    title = models.CharField(max_length=100)
    state = models.CharField(choices=IssueState, default=IssueState.TODO)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title
