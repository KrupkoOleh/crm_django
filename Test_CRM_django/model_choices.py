from django.db.models import TextChoices


class Status(TextChoices):
    DONE = 'DONE', 'виконаний'
    UNDONE = 'UNDONE', 'не виконаний'
