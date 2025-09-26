from django.db import models

from Test_CRM_django.mixins.models import PKMixin
from Test_CRM_django.model_choices import Status


class Projects(PKMixin):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name',)


class Tasks(PKMixin):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    deadline = models.DateTimeField(null=True,
                                    blank=True)
    priority = models.PositiveIntegerField(editable=False, null=True, blank=True)
    status = models.CharField(
        max_length=100,
        choices=Status.choices,
        default=Status.UNDONE
    )

    class Meta:
        ordering = ['priority']
        unique_together = ('name', 'project')


def __str__(self):
    return self.name
