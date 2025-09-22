from django.db.models.aggregates import Max
from django.db.models.signals import pre_save
from django.dispatch import receiver

from projects.models import Tasks


@receiver(pre_save, sender=Tasks)
def set_priority(sender, instance, **kwargs):
    if instance._state.adding and instance.priority is None:
        max_priority = Tasks.objects.aggregate(Max('priority'))['priority__max']
        instance.priority = (max_priority or 0) + 1
